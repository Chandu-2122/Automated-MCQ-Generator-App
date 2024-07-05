import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_data, get_quiz_table
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

#loading output as json file
with open('C:\\Users\\chand\\mcq_generator\\response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

#title of the app
st.title('Automated MCQ Generator App')
 
#input form
with st.form("user_input"):
    #upload file
    uploaded_file = st.file_uploader("Upload a PDF or a txt file")
     
    #mcqs count
    mcq_count = st.number_input("Number of MCQs to be generated", min_value=4, max_value=50)
    #subject
    subject = st.text_input("Subject Name", max_chars=20)
    #mcqs complexity tone
    tone = st.text_input("Complexity level of Questions", max_chars=20, placeholder="Simple")
     
    #Submit button
    button = st.form_submit_button("Generate MCQs")
     
    #on clicking submit button
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating MCQs..."):
            try:
                text = read_data(uploaded_file)
                 
                #tokens count and cost of API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
                
            except Exception as e:
                traceback.print_exception(type(e),e, e.__traceback__)
                st.error("Error")
                
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Response Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    #extract quiz data from response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_quiz_table(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index +1
                            st.table(df)
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the Table data")
                else:
                    st.write(response)
                                
            