import streamlit as st

app = st.selectbox('Select App', ['Latest Movies'])

def app ():
    st.write("Thanks for using this app!")
    st.write("Prosceed by clicking the link below")
    st.markdown("[Login/Register on MDB API](https://mdbapi.com/login)", unsafe_allow_html=True)
    
if app == 'Latest Movies':
    app()
