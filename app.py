import streamlit as st
import pandas as pd

from nbformat import read, NO_CONVERT

# Load movie data from CSV file
@st.cache
def load_movie_data(file_path):
    movie_data = pd.read_csv('movies_metadata.csv')
    return movie_data['name']

# Recommender function
def recommend(favorite_movie):
    notebook_path = 'recommender.ipynb'
    notebook = read(open(notebook_path), NO_CONVERT)

    exec('\n'.join([cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']), globals())

    return recommend(favorite_movie)

def main():

    st.title("Movie Recommender System")

    folder_path = st.text_input("Enter the folder path")
    file_name = st.text_input("Enter the file name (including .csv)")
    
    if folder_path and file_name:
        try:
            # Construct the file path
            file_path = folder_path.rstrip("/") + "/" + file_name

            movie_data = load_movie_data(file_path)

            # Display DataFrame
            st.write(df)

        except FileNotFoundError:
            st.error("File not found. Please check the folder path and file name.")
    # Load movie data
    # movie_data = load_movie_data(folder_path)

    # # User input
    # favorite_movie = st.multiselect("Select your favorite movie", movie_data['movie'])

    # if st.button("Get Recommendations"):
    #     recommendations = recommend(favorite_movie)
    #     st.write("Recommended Movies:")
    #     for movie in recommendations:
    #         st.write(movie)

if __name__ == "__main__":
    main()
