import streamlit as st
import pandas as pd
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, NO_CONVERT
import pickle
import requests

# Load movie data from CSV file
@st.cache_data 
def load_movie_data(file_path):
    movie_data = pd.read_csv('movies_metadata.csv')
    movie_data = movie_data.sort_values('title') 
    return movie_data['title']

# Recommender function
def recommend(favorite_movie):
    

    return "1","2","3"

movies = pickle.load(open("movies.pkl", 'rb'))
movies_date = list( movies['release_date'])
movies_list=list(movies['title'] )
movies_list = [i+' '+str(j.year) for i,j in zip(movies_list,movies_date)]


def main():

    with st.sidebar:
        st.title("Movie Recommender Pro")
        st.subheader("Developer:")
        st.markdown("<a href='https://www.linkedin.com/in/sepehr-mousaviyan-8baa7b1ab/'>Sepehr mousaviyan</a>", unsafe_allow_html=True)
        st.markdown("Checkout my colab for see full version of many methods:")
        st.markdown("<a href='https://colab.research.google.com/drive/1IHZME7w9EF9goinIpZXCOkhv3CX0RexU#scrollTo=YzbmNPo673-Q'>Note book link</a>", unsafe_allow_html=True)

    st.title("Movie Recommender System")

    file_path = "movie_metadata.csv"
    
    # st.write(file_path)
    movie_data = load_movie_data(file_path)

    favorite_movie = st.multiselect("Select your favorite movies(at least 3 movies)", movie_data)

    if st.button("Get Recommendations"):
        recommendations = recommend(favorite_movie)
        st.write("Recommended Movies:[Just made for you:)]")
        for movie in recommendations:
            st.write(movie)

if __name__ == "__main__":
    main()
