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
    notebook_path = 'Copy of Copy of Recommender.ipynb'
    notebook = read(open(notebook_path), NO_CONVERT)

    exec('\n'.join([cell['source'] for cell in notebook['cells']]), globals())

    return get_recommendations(favorite_movie).head(5)


def execute_notebook_sections(notebook_path, sections):
    # Read the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Create a preprocessor to execute the notebook
    preprocessor = ExecutePreprocessor(timeout=600)

    # Iterate over the notebook cells
    for cell in notebook.cells:
        if cell.cell_type == "code":
            
            cell_metadata = cell.metadata
            st.write(cell)

            # Execute the cell if it has the desired section metadata
            if "section" in cell_metadata and cell_metadata["section"] in sections:
                st.write("here")
                preprocessor.preprocess_cell(cell, {"metadata": cell_metadata})

    # Save the executed notebook
    with open("executed_notebook.ipynb", "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)




def main():

    movies = pickle.load(open("movies.pkl", 'rb'))
    movies_date = list( movies['release_date'])
    movies_list=list(movies['title'] )
    movies_list = [i+' '+str(j.year) for i,j in zip(movies_list,movies_date)]
    with st.sidebar:
        # logo = Image.open("")
        # st.image(logo, caption='MM Movie Recommender')
        st.title("Movie Recommender Pro")
        st.subheader("Development Team:")
        st.markdown("<a href='https://www.linkedin.com/in/sepehr-mousaviyan-8baa7b1ab/'>Sepehr mousaviyan</a>", unsafe_allow_html=True)
        st.markdown("This app uses ---- model, checkout my colab full version of many methods that i implemented")

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
    
    # st.write(file_path)
    movie_data = load_movie_data(file_path)

    # Display DataFrame
    # st.write(movie_data)
    
    # Load movie data


    # # User input
    favorite_movie = st.multiselect("Select your favorite movie", movie_data)
    
    if len(favorite_movie) ==1:
        col1 , col2 = st.columns([1,3])
        t1 =movies.iloc[movies_list.index(favorite_movie[0])]['imdb_id']
        
        url = f"http://www.omdbapi.com/?i={t1}&apikey=9c7662c4"
        re = requests.get(url).json()
        if('N/A' in re['Poster']):
            re['Poster']='./404.jpg'
        with col1:
            st.image(re['Poster'], width=100)
        with col2:
            st.write(re['Title']+ "(" + re['Year'] + ")")
            st.caption(f"Genres: {re['Genre']}")


    if st.button("Get Recommendations"):

        # notebook_path = "Recommender.ipynb"
        # sections_to_execute = ["Import required libaries", "Content based"]
        
        # execute_notebook_sections(notebook_path, sections_to_execute)
        recommendations = recommend(favorite_movie)
        # st.write("Recommended Movies:")
        # for movie in recommendations:
        #     st.write(movie)

if __name__ == "__main__":
    main()
