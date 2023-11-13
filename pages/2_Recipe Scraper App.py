import openai
import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

st.sidebar.title("_Recipe Scraper_")
st.title("_AI Web Recipe Scraper_")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
try:
    # Create a sidebar for user input
    url = st.sidebar.text_input("Enter URL for recipe:")
    if st.sidebar.button("Generate Markdown"):
        text = f"""
        Visit the website at the following URL: {url}
        """
        prompt = f"""
        From the text below, please understand it as an article that describes a recipe.  
        The first line should be: "<recipe name>". A new line will be inserted then the word "Ingredients:" 
        followed by each line should contain one ingredient and its amount in the format
        "<ingredient>: <amount>". The ingredient part (before the semicolon) should contain only the ingredient name, not the amount.
        Next is the "Instructions:" section.  Each line should be a numbered list for each step.  And lastly, there may be a notes section. 
        If there is, it should be titled "Notes:" with a paragraph after. 
        Add another new line saying "For the full recipe and more details, visit the website at the following URL:" and follow with the 
        url as a hyperlink.
        The text is: 
        ```{text}```
        """
        response = get_completion(prompt)
        st.title(response.split('\n')[0])
        st.write("---")
        st.write(response[response.index('\n')+1:])

        with open(os.path.join("/Volumes/homes/Melissa/Drive/SynologyDrive/Work/NLP projects/Cookbook/PrintedRecipes",response.split('\n')[0]+".md"), "w") as file:
            file.write(response)


    # Save as a Markdown file
    file_name = response.split('\n')[0]
    path = "/Volumes/homes/Melissa/Drive/SynologyDrive/Work/NLP projects/Cookbook/PrintedRecipes"
    with open(os.path.join(path,file_name+".md"), "w") as file:
        file.write(response)
        st.success(f"Markdown file '{file_name}.md' has been saved.")

except NameError:
    st.success("Enter URL in the left sidebar")


