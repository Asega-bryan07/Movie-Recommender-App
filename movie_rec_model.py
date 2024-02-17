# -*- coding: utf-8 -*-
"""Movie__rec_model.ipynb

# MOVIE RECOMMENDER MODEL - BRYAN ASEGA
Using Cosine Similarity

## Libraries and Data
"""

# importing dependencies
import os
import pandas as pd
import ast
import gdown
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

"""### Dataset and API
```Accessed from: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata```<br>
```MovieDB API:```
"""

# Replace the file_id with the actual file ID from your Google Drive link

credits_data = os.environ.get("CREDITS_DATA")
movies_data = os.environ.get("MOVIES_DATA")


# Get the direct download link
url1 = f'https://drive.google.com/uc?id={credits_data}'
url2 = f'https://drive.google.com/uc?id={movies_data}'

# Download the file to the current working directory
credit = 'credits_data.csv'
movie = 'movies_data.csv'
gdown.download(url1, credit, quiet=False)
gdown.download(url2, movie, quiet=False)

# Read the CSV files into Pandas DataFrames
credits = pd.read_csv(credit)
movies = pd.read_csv(movie)

movies = movies.merge(credits, on='title')

# columns to use for recommendation
movies = movies[['genres', 'keywords', 'overview', 'title', 'movie_id',	'cast',	'crew']]

# checking for empty cells
# movies.isnull().sum()

# overview has three empty cells, dropping it will not impact the dataset heavily
movies.dropna(inplace=True)

# handling the genre column
movies.iloc[0]['genres']

# convert string to a list
def conv_str_tolist(text):
  list_ = []
  for i in ast.literal_eval(text):
    list_.append(i['name'])
  return list_

movies['genres'] = movies['genres'].apply(conv_str_tolist)

# handling the keywords column
movies.iloc[0]['keywords']

movies['keywords'] = movies['keywords'].apply(conv_str_tolist)

# handling the cast column
movies.iloc[0]['cast']

# to kee pthe top three casts
def convert_to_cast(text):
  list_c = []
  counter = 0
  for i in ast.literal_eval(text):
    if counter < 3:
      list_c.append(i['name'])
    counter += 1
  return list_c

movies['cast'] = movies['cast'].apply(convert_to_cast)

# handling the crew column
movies.iloc[0]['crew']

def fetch_director(text):
  list_ = []
  for i in ast.literal_eval(text):
    if i['job'] == 'Director':
      list_.append(i['name'])
      break
  return list_

movies['crew'] = movies['crew'].apply(fetch_director)

# handling the overview column
movies.iloc[0]['overview']

movies['overview'] = movies['overview'].apply(lambda x: x.split())

# handling the overview column
movies.iloc[0]['overview']

# removing spaces
def remove_spaces(list_):
  list_r = []
  for i in list_:
    list_r.append(i.replace(" ",""))
  return list_r

movies['cast'] = movies['cast'].apply(remove_spaces)
movies['crew'] = movies['crew'].apply(remove_spaces)
movies['genres'] = movies['genres'].apply(remove_spaces)
movies['keywords'] = movies['keywords'].apply(remove_spaces)

# bringing all of them together
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

movies.iloc[0]['tags']

df = movies[['movie_id', 'title', 'tags']] # to a dataframe

# convert to string from a list
df['tags'] = df['tags'].apply(lambda x: " ".join(x))

df.iloc[0]['tags']

# convert to string to lowecase
df['tags'] = df['tags'].apply(lambda x: x.lower())

df.iloc[0]['tags'] # now its in small letters

ps = PorterStemmer()

def stems(text):
  stem_ = []
  for i in text.split():
    stem_.append(ps.stem(i))

  return " ".join(stem_)

df['tags'] = df['tags'].apply(stems)

df.iloc[0]['tags']

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(df['tags']).toarray()

#checking length of feature names
# len(cv.get_feature_names_out())

"""## Cosine Similarity"""

similarity = cosine_similarity(vectors)


df[df['title'] == 'The Lego Movie'].index[0]

"""it works fine with the cosine similarity<br>
## Recommend a Movie
"""

# def recommend_movie(movie):
#   sim_index = df[df['title'] == movie].index[0]
#   dist = sorted(list(enumerate(similarity[sim_index])), reverse=True,key = lambda x: x[1])
#   for i in dist[1:6]:
#     print(df.iloc[i[0]].title)

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x: x[1])
    for i in distances[1:6]:
        print(df.iloc[i[0]].title)

"""Testing the Recommendation"""

# recommend_movie('Bat-Man')

"""# Save the models
Using the pickle dependency
"""

# Save the similarity and movie list models
pickle.dump(df,open('./movie_list.pkl','wb'))
pickle.dump(similarity,open('./similarity.pkl','wb'))

"""# DONE!"""
