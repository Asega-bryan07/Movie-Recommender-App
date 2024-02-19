'''
Author: BRYAN ASEGA
Email: Almasibryan7@gmail.com
Date: 2024-02-05 14:31:59
'''
import pandas as pd
import pickle
import streamlit as st
import requests

def main():
    # Set page configuration
    st.set_page_config(
    page_title="MOVIE RECOMMENDER APP - AI+",
    page_icon="⭐", layout="wide",)
    

    # Sidebar with profile image and name
    st.sidebar.image(
        "./profile/profile.jpg",
        width=150,
        caption="BY: ENG. BRYAN ASEGA\n\n""\n"
                "This app was developed purposely for movie recommendations. A user of the "
                "app has the ability to prompt the app to suggest the movie of choice. However, ""\n"
                "Multiple genres cannot be selected at the moment. This is an improvement that will take "
                "shape in the next few days.\n\n""\n"
                "Enjoy the app. Cheers! :)\n""\n"
                "To access the codes and deployment pipeline, please visit my github page: ""\n"
                "[https://github.com/asega-bryan07/movie-recommender-app](https://github.com/asega-bryan07/movie-recommender-app) "
                # "or scan the QR-Code below:\n"
                # "./profile/logo.jpg"
    )
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
        # url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=309943535d3920914514333830997333&language=en-US"
        # response = requests.get(url)
        # data = response.json()
        # poster_path = data['poster_path']
        # full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        # return full_path


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

    
    st.header('MOVIE RECOMMENDER APP')

    with open("model/movie_list.pkl", "rb") as mfile:
        movies = pd.read_pickle(mfile)
    with open("model/similarity.pkl", "rb") as sfile:
        similarity = pd.read_pickle(sfile)
    

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

    
    st.markdown(
        """
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-jNvQoi8KVSo+6hgeowkEldHO/UqWT9g/BvTy9vquAs7iMq/n79Zo1EHrYKgJy6OL3h0CFtikBKr6ZaEy5+gU5A==" crossorigin="anonymous" />
        </head>
        <style>
            body {
                background-color: #orange;  
            }
            .footer {
                display: flex;
                justify-content: space-around;
                align-items: center;
                position: fixed;
                bottom: 0;
                width: 100%;
                padding: 10px;
                background-color: #f1f1f1;
            }
            .social-icon {
                font-size: 24px;
                margin-right: 10px;
            }
        </style>
        <div style="display: flex; justify-content: center; align-items: center; padding-top: 20px;">
            <a href="#https://github.com/Asega-bryan071#" target="_blank" class="social-icon"><i class="fab fa-github"></i></a> <!-- GitHub icon -->
            <a href="https://www.linkedin.com/in/asega-bryan-ba7781224/" target="_blank" class="social-icon"><i class="fab fa-linkedin"></i></a> <!-- LinkedIn icon -->
            <a href="https://medium.com/@almasibryan" target="_blank" class="social-icon"><i class="fab fa-medium"></i></a> <!-- Medium icon -->
            <a href="your_twitter_link" target="_blank" class="social-icon"><i class="fab fa-twitter"></i></a> <!-- Twitter icon -->
            <a href="https://wa.me/+254793681980/" target="_blank" class="social-icon"><i class="fab fa-whatsapp"></i></a> <!-- WhatsApp icon -->
            <a href="https://www.facebook.com/victor.mainakimani?mibextid=rS40aB7S9Ucbxw6v" target="_blank" class="social-icon"><i class="fab fa-facebook"></i></a> <!-- Facebook icon -->
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
