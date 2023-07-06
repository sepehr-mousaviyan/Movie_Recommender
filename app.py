import streamlit as st
import pandas as pd
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, NO_CONVERT

# Load movie data from CSV file
@st.cache
def load_movie_data(file_path):
    movie_data = pd.read_csv('movies_metadata.csv')
    movie_data = movie_data.sort_values('title') 
    # st.write(movie_data)
    return movie_data['title']

# Recommender function
def recommend(favorite_movie):
    notebook_path = 'Copy of Copy of Recommender.ipynb'
    notebook = read(open(notebook_path), NO_CONVERT)

    exec('\n'.join([cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']), globals())

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
