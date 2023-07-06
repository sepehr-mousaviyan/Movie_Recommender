import streamlit as st
import pandas as pd
import os

from nbformat import read, NO_CONVERT

# Load movie data from CSV file
@st.cache
def load_movie_data(file_path):
    movie_data = pd.read_csv('movies_metadata.csv')
    # st.write(movie_data)
    return movie_data['title']

# Recommender function
def recommend(favorite_movie):
    notebook_path = 'recommender.ipynb'
    notebook = read(open(notebook_path), NO_CONVERT)

    exec('\n'.join([cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']), globals())

    return recommend(favorite_movie)

def main():

    st.title("Movie Recommender System")

    # # Get current directory contents
    # dir_contents = os.listdir()

    # # Display directory contents
    # st.write("Directory Contents:")
    # for item in dir_contents:
    #     st.write(item)
    
    # cwd = os.getcwd()

    # # Display current working directory
    # st.write("Current Working Directory:", cwd)
    # folder_path = st.text_input("Enter the folder path")
    # file_name = st.text_input("Enter the file name (including .csv)")
    

    # Construct the file path
    file_path = "movie_metadata.csv"
    
    st.write(file_path)
    movie_data = load_movie_data(file_path)

    # Display DataFrame
    st.write(movie_data)
    
    # Load movie data


    # # User input
    favorite_movie = st.multiselect("Select your favorite movie", movie_data)

    # if st.button("Get Recommendations"):
    #     recommendations = recommend(favorite_movie)
    #     st.write("Recommended Movies:")
    #     for movie in recommendations:
    #         st.write(movie)

if __name__ == "__main__":
    main()
