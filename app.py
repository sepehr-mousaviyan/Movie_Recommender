import streamlit as st
import pandas as pd
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, NO_CONVERT
import pickle
import requests


@st.cache_data 
def load_movie_data(file_path):
    movie_data = pd.read_csv('movies_metadata.csv')
    movie_data = movie_data.sort_values('title') 
    return movie_data['title']

def fetch_poster(movie_id):
    #Using leaked key
    response = requests.get('https://api.themoviedb.org/3/movie/{0}?api_key=d61204e42321cddd34e0f954c0bf649f&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

# Recommender function
def recomend(movie):
    for moviei in movies:
        if (moviei['title'] == movie):
            movie_index = movie.index[0]
    # movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recomendedMovies = []
    recomended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recomendedMovies.append(movies.iloc[i[0]].title)
        recomended_movies_posters.append(fetch_poster(movie_id))
    return  recomendedMovies, recomended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


def main():

    with st.sidebar:
        st.title("Movie Recommender Pro")
        st.subheader("Developer:")
        st.markdown("<a href='https://www.linkedin.com/in/sepehr-mousaviyan-8baa7b1ab/'>Sepehr mousaviyan</a>", unsafe_allow_html=True)
        st.markdown("Checkout my colab for see full version of many methods:")
        st.markdown("<a href='https://colab.research.google.com/drive/1IHZME7w9EF9goinIpZXCOkhv3CX0RexU#scrollTo=YzbmNPo673-Q'>Note book link</a>", unsafe_allow_html=True)

    st.title("Movie Recommender System")


    selected = st.multiselect("Select your favorite movies(at least 3 movies)", movies['title'].values)

    if st.button("Get Recommendations"):
        recomend_movies, poster = recomend(selected)
        st.write("Recommended Movies:[Just made for you:)]")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recomend_movies[0])
            st.image(poster[0])
        with col2:
            st.text(recomend_movies[1])
            st.image(poster[1])
        with col3:
            st.text(recomend_movies[2])
            st.image(poster[2])
        with col4:
            st.text(recomend_movies[3])
            st.image(poster[3])
        with col5:
            st.text(recomend_movies[4])
            st.image(poster[4])

if __name__ == "__main__":
    main()
