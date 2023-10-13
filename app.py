from io import BytesIO
import base64
import streamlit as st 
import requests
from PyPDF2 import PdfReader
import openai

import os

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

api_key =  st.secrets['OPENAI_API_KEY']

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

            prompt1 = "Look at the resume given.  Show each data under its relevant heading in json format. The resume is :"
            prompt2 = "Extract and display the details of the person's current role or most recent role, including the Role Name, Company, and Duration. If there's no end date specified for the current role, assume it's an ongoing role. Only display this for one role. The data is : "
            prompt3 = "Write a first person work profile/summary from the data given so that it showcases the following values : Personal Impact,Entrepreneurial Drive,Inclusive Leadership,Courageous Change, Problem Solving, Expertise. Do not repeat the values as they are, and it need not include all the values. Limit to less than 50 words. The data is :"
            prompt4 = "Extract the educational background from this and ask the users if any of the following missing entries Degree,Institution ,GPA/Percentage ,Year for each education are present. and don't give me any extra suggestions "
            prompt5 = "Extract the skills from the above resume and make sure that the skills are relevant for management consulting resumes. Remove the skills that are not relevant. If no skills match the description, ask the user to enter at least three skills. Limit the skills to 4 and each skill should not exceed 3 words.If skills are lacking, suggest new skills."
            prompt6 = "Extract the extracurricular activities from the above resume. Extracurricular activities are the activities not part of professional or educational activities. These are usually hobbies, and other activities done for fun. Limit to displaying only 5 activities if there are too many extracurriculars. Only show a heading for each extracurricular activity. If there are no such activities,display '''No Extracurriculars''' and ask the user to enter the activities in any of the following categories Cultural,Volunteer,Musical activities,Miscellaneous,Sports"
            prompt7 = "Extract the work experience from the resume and and put it in chronological order"
    
            list_of_prompts=[prompt1,prompt2,prompt3,prompt4,prompt5,prompt6,prompt7]
          
            #Resume Segmentation
            prompt_1=list_of_prompts[0] + text
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_1,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            output = response.choices[0].text.strip()

            #Current Role
            prompt_2=list_of_prompts[1] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_2,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            format="The current role you are working in :"
            st.header(format)
            st.write(outputs)
            
           #Work Summary
            prompt_3=list_of_prompts[2] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_3,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            format="Your work summary is :"
            st.header(format)
            st.write(outputs)

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



