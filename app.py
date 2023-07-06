import streamlit as st

# Load movie data
# ...

# Build the recommender system
# ...

# Streamlit app
def main():
    st.title("Movie Recommender System")

    # User input
    user_preferences = st.multiselect("Select your preferences", ["Action", "Comedy", "Drama"])

    if st.button("Get Recommendations"):
        recommendations = get_recommendations(user_preferences)
        st.write("Recommended Movies:")
        for movie in recommendations:
            st.write(movie)

if __name__ == "__main__":
    main()
