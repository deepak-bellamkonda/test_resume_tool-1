from io import BytesIO
import base64
import streamlit as st 
import requests
from PyPDF2 import PdfReader
import openai
from prompts import *

openai.api_key = st.secrets['OPENAI_API_KEY']
completion = openai.ChatCompletion()

st.markdown("""
<style>
/* CSS for the title container */
.title-container {
    
    background-image: url('logo.jpeg');
    background-size: cover;
    text-align: center;
    padding: 20px;
    border-radius: 10px;
}

/* CSS for the title text */
.title-text {
    font-size: 36px;
    color: black;
    font-weight: bold;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='title-container'><p class='title-text'>Resume Recommendation Tool</p></div>", unsafe_allow_html=True)
st.write("Please upload your resume in PDF format.")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if st.button("Submit"):
            if uploaded_file is not None:
                st.success("You have successfully uploaded your resume:wink::wink:.")
                st.header("Resume content")
                pdf_reader = PdfReader(uploaded_file)
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    #text += page.extract_text()
                    text = "\n".join([text,page.extract_text()])

                #st.write(text)

                #st.write(decoded_content)
            else:
                st.write("Error occured,please Try again!")
            
            #Resume Segmentation
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_segment},
                {"role": "user","content": text}
                ],
                temperature = 0
            )
            segment = response.choices[0]['message']['content']
    
            #Current Role
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_currentrole_display},
                {"role": "user","content": segment}
                ],
                temperature = 0
            )
    
            current_role = response.choices[0]['message']['content']
            format="The current role you are working in :"
            st.header(format)
            st.write(current_role)
            
            #Work Summary - Display
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_summary_display},
                {"role": "user","content": segment}
                ],
                temperature = 0
            )
    
            summary = response.choices[0]['message']['content']
            format="Your work summary is :"
            st.header(format)
            st.write(summary)

            #Work Summary - Suggest
            suggest_summary = st.radio(
                "How do you wish to rewrite the summary?",
                [
                    " Make it data heavy with blanks to supply data",
                    " Highlight the soft skills of the resume",
                    " Highlight the industry diversity and experience"
                ]
            )

            if st.button("Submit"):
    
            #Work Summary - Rewrite
                prompt_summary_rewrite += suggest_summary
                response = completion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    { "role": "system","content": prompt_summary_rewrite},
                    {"role": "user","content": summary}
                    ],
                    temperature = 0
                )
        
                rewrite_summary = response.choices[0]['message']['content']
                format="Your rewritten work summary is :"
                st.header(format)
                st.write(rewrite_summary)
    
            #Educational Background
            '''prompt_4=list_of_prompts[3] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_4,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            format="Your Educational Details are as follows : "
            st.header(format)
            st.write(outputs)

            #Skills
            prompt_5=list_of_prompts[4] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_5,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            format="Your skills are as follows :"
            st.header(format)
            st.write(outputs)

            #Extracurriculars
            prompt_6=list_of_prompts[5] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_6,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            format="Your Extracurriculars are as follows : "
            st.header(format)
            st.write(outputs)

            prompt_7=list_of_prompts[6] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_7,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            format="Your Extracurriculars are as follows : "
            st.header(format)
            st.write(outputs)'''



