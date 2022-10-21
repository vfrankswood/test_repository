import streamlit as st
from utils import *

st.header('Good News Paper')


genres = get_genres()

selected_genre = st.sidebar.selectbox(label='Select genre of article to read', options=[None]+genres)
if not selected_genre:
    st.write('Please choose genre')
    st.stop()
article = get_article(selected_genre)
st.write(article)



