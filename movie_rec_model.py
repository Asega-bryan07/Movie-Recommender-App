# -*- coding: utf-8 -*-
"""

# MOVIE RECOMMENDER MODEL - BRYAN ASEGA<br>
Using Cosine Similarity

"""

"""### Dataset and API
```Accessed from: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata```<br>
```MovieDB API:```

## Libraries and Data
"""
# importing dependencies
import pandas as pd
import ast
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocessing():
  credits = pd.read_csv('C:/Users/HERLAB26/Documents/Desktop/Movie-Recommender-App/Flask App/data/tmdb_5000_credits.csv')
  movies = pd.read_csv('C:/Users/HERLAB26/Documents/Desktop/Movie-Recommender-App/Flask App/data/tmdb_5000_movies.csv')

  movies = movies.merge(credits, on='title')
  # columns to use for recommendation
  movies = movies[['genres', 'keywords', 'overview', 'title', 'movie_id',	'cast',	'crew']]

  # checking for empty cells
  movies.isnull().sum()

  # overview has three empty cells, dropping it will not impact the dataset heavily
  movies.dropna(inplace=True)
  movies.isnull().sum()


  # check duplicates in movies
  movies.duplicated().sum()

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
  movies.head(2)

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
  movies.sample(5)

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

  df['tags'] = df['tags'].apply(stems).copy()


  df.iloc[0]['tags']

  cv = CountVectorizer(max_features=5000, stop_words='english')

  vectors = cv.fit_transform(df['tags']).toarray()
  vectors[0]

  vectors.shape

  #checking length of feature names
  len(cv.get_feature_names_out())

  """## Cosine Similarity"""
  similar=cosine_similarity(vectors)



  df[df['title'] == 'The Lego Movie'].index[0]

  """it works fine with the cosine similarity<br>
  ## Recommend a Movie
  """
  def recommend(movie):
      index = df[df['title'] == movie].index[0]
      distances = sorted(list(enumerate(similar[index])),reverse=True,key=lambda x: x[1])
      for i in distances[1:6]:
          print(df.iloc[i[0]].title)

"""Testing the Recommendation"""

# recommend('Arachnophobia')
