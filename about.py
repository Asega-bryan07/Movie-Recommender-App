import streamlit as st

def app():
    st.subheader('The Movie Recommender App was developed purposely for movie recommendations.')
    st.subheader('A user of the app has the ability to prompt for a movie of choice. However, \
               Multiple genres cannot be selected at the moment. This is an improvement that will take\
               shape in the next few days.\n\
               Enjoy the app. Cheers! :)\n\
               To access the codes and deployment pipeline, please visit my github page: ')
    st.markdown('Created by: [ENG. ASEGA BRYAN](https://github.com/asega-bryan07/movie-recommender-app)')
    st.markdown('Contact via mail: [Almasibryan7@gmail.com@gmail.com]')

if __name__ == '__main__':
    app()