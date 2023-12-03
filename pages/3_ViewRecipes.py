import streamlit as st
import os

# Define the directory containing your Markdown files
current_file_directory = os.path.dirname(__file__)
markdown_dir = os.path.join(current_file_directory, '..',"PrintedRecipes")  # Use quotes or underscore

# Get a list of all Markdown files in the directory
markdown_files = [file for file in os.listdir(markdown_dir) if file.endswith(".md")]

# Sidebar to search for a Markdown file by name
search_query = st.sidebar.text_input("Search for a Recipe by keywords")
filtered_files = [file for file in markdown_files if search_query.lower() in file.lower()]

# Dropdown to select a Markdown file
selected_file = st.sidebar.selectbox("Select a Recipe", [""] + filtered_files)

# Run the Streamlit app
if __name__ == "__main__":
    st.title("_View Saved Recipes:_")
    # st.sidebar.markdown("### Choose a Markdown file to view:")

# Read and display the selected Markdown file
if selected_file:
    with open(os.path.join(markdown_dir, selected_file), "r") as file:
        markdown_content = file.read()
        st.markdown(markdown_content)

st.download_button(
    label="Download Recipe",
    data=st.markdown(markdown_content),
    file_name=selected_file+".md"
)