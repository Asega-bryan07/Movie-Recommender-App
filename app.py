
'''
Author: BRYAN ASEGA
Email: Almasibryan7@gmail.com
Date: 2024-02-05 14:31:59
'''

# Dependencies to use
import pandas as pd
import streamlit as st
import requests
from streamlit_option_menu import option_menu
import about, my_profile, mdbconnect

# Set page configuration
st.set_page_config(
    page_title="MOVIE RECOMMENDER APP - AI+",
    page_icon="⭐",
    layout="wide"
)

class MovieApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Sidebar with profile image and name
        with st.sidebar:
            app = option_menu(
                menu_title='THE MOVIE RECOMMENDER APP',
                options=['Home', 'Developer', 'Latest Movies'],
                icons=['house-fill', 'person-circle', 'trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "3!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "18px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

            if app == 'Home':  # About the app
                about.app()
            if app == 'Developer':  # my profile
                my_profile.app()
            if app == 'Latest Movies':  # connect to tmdb
                mdbconnect.app()

        def fetch_poster(movie_id):
            url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
            data = requests.get(url)
            data = data.json()
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path

        st.header('MOVIE RECOMMENDER APP')

        with open("model/movie_list.pkl", "rb") as mfile:
            movies = pd.read_pickle(mfile)
        with open("model/similarity.pkl", "rb") as sfile:
            similarity = pd.read_pickle(sfile)

        def recommend(movie):
            index = movies[movies['title'] == movie].index[0]
            distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x: x[1])
            recommended_movie_names = []
            recommended_movie_posters = []
            for i in distances[1:6]:
                movie_id = movies.iloc[i[0]].movie_id
                recommended_movie_names.append(movies.iloc[i[0]].title)
                recommended_movie_posters.append(fetch_poster(movie_id))
            return recommended_movie_names, recommended_movie_posters

        movie_list = movies['title'].values
        selected_movie = st.selectbox('Type or Select a Movie Name 😎\n', movie_list)
        if st.button('Recommended Movie'):
            recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommended_movie_names[0])
                st.image(recommended_movie_posters[0])
            with col2:
                st.text(recommended_movie_names[1])
                st.image(recommended_movie_posters[1])
            with col3:
                st.text(recommended_movie_names[2])
                st.image(recommended_movie_posters[2])
            with col4:
                st.text(recommended_movie_names[3])
                st.image(recommended_movie_posters[3])
            with col5:
                st.text(recommended_movie_names[4])
                st.image(recommended_movie_posters[4])

                '''Latest Version Coming Soon'''
                '''AI+'''

# Create an instance of the MovieApp class and run the app
movie_app = MovieApp()
movie_app.run()
