import streamlit as st
import pandas as pd

from nbformat import read, NO_CONVERT

# Load movie data from CSV file
@st.cache
def load_movie_data():
    movie_data = pd.read_csv('movies_metadata.csv')
    return movie_data

# Recommender function
def recommend(favorite_movie):
    notebook_path = 'recommender.ipynb'
    notebook = read(open(notebook_path), NO_CONVERT)

    exec('\n'.join([cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']), globals())

    return recommend(favorite_movie)

def main():

    st.title("Movie Recommender System")
    
    # Load movie data
    movie_data = load_movie_data()


    # User input
    favorite_movie = st.multiselect("Select your favorite movie", movie_data['movie'])

    if st.button("Get Recommendations"):
        recommendations = recommend(favorite_movie)
        st.write("Recommended Movies:")
        for movie in recommendations:
            st.write(movie)

if __name__ == "__main__":
    main()
