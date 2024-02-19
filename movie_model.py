# -*- coding: utf-8 -*-

'''# MOVIE RECOMMENDER APP - BRYAN ASEGA<br>

#Using Cosine Similarity'''

## Libraries and Data


# importing dependencies
import pandas as pd
import streamlit as st
import ast
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""### Dataset and API
```Accessed from: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata```<br>
```MovieDB API:```
"""

credits = pd.read_csv('./data/tmdb_5000_credits.csv')
movies = pd.read_csv('./data/tmdb_5000_movies.csv')

movies = movies.merge(credits, on='title')

# columns to use for recommendation
movies = movies[['genres', 'keywords', 'overview', 'title', 'movie_id',	'cast',	'crew']]

# overview has three empty cells, dropping them will not impact the dataset heavily
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
movies.head()

# bringing all of them together
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# movies.head(3)

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
vectors[0]

#checking length of feature names
len(cv.get_feature_names_out())

"""## Cosine Similarity"""

similarity = cosine_similarity(vectors)

similarity.shape

df[df['title'] == 'The Lego Movie'].index[0]

"""it works fine with the cosine similarity<br>
## Recommend a Movie
"""

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x: x[1])
    for i in distances[1:6]:
        print(df.iloc[i[0]].title)