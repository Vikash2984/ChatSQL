import streamlit as st
import sqlite3
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI

# Configure Gemini API Key
api_key = "AIzaSyDG1Z35te8uvWSRnZNtNRIte_bQCilsFJw"

# Initialize the Google Gemini model
llm_1 = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-pro")

# Setup SQLDatabase
input_db = SQLDatabase.from_uri('sqlite:///dataset.db')

# Prompt for Gemini
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
The SQL database has the name AEC and has the following columns: Name, Specialization, HOD.

For example:
Example 1 - How many entries of records are present?
The SQL command will be something like this: SELECT COUNT(*) FROM AEC;

Example 2 - Tell me all the students specializing in AIML?
The SQL command will be something like this: SELECT * FROM AEC WHERE Specialization = "AIML";

Example 3 - Whenever a question starts with "who is" the result must be one unique value
NOTE : If the databse returns duplicate data for any asked question return the value once and only once

Example 4 - Whenever asked to insert records such as "Insert a new record with student name Vikash specilization AIML and HOD ABN
The SQL command will be something like this: INSERT INTO AEC VALUES("Vikash","AIML","ABN");

The SQL code should not have ``` in the beginning or end, and avoid using the word "SQL" in the output.
    """
]

# Function to get response from Gemini
def get_gemini_response(question, prompt):
    response = llm_1.invoke(f"{prompt[0]} {question}")
    return response.content

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")
# st.header("Data Bridge (ᵖᵒʷᵉʳᵉᵈ ᵇʸ Gemini©)")
st.header("Data Bridge (ᵖᵒʷᵉʳᵉᵈ ᵇʸ Gemini)")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    # Get the SQL query from the Gemini model
    sql_query = get_gemini_response(question, prompt)
    
    # Retrieve results from the database
    conn = sqlite3.connect('dataset.db')
    cur = conn.cursor()
    cur.execute(sql_query)  # Execute the extracted SQL query
    rows = cur.fetchall()
    conn.close()
    
    # Display results
    st.subheader("The Response is")
    for row in rows:
        st.write(row)