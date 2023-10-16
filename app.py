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
            h1 ="Current Role"
            sh1 = "What you have written"
            st.header(h1)
            st.subheader(sh1)
            st.write(current_role)
            
            #Work Summary
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_summary_display},
                {"role": "user","content": segment}
                ],
                temperature = 0
            )
    
            summary = response.choices[0]['message']['content']
            
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_summary_rewrite},
                {"role": "user","content": summary}
                ],
                temperature = 0
            )
    
            summary_rewrite = response.choices[0]['message']['content']

            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_summary_suggest},
                {"role": "user","content": summary_rewrite}
                ],
                temperature = 0
            )
    
            summary_suggest = response.choices[0]['message']['content']
            
            h1 ="Work Summary"
            sh1 = "What you have written"
            sh2 = "What we suggest"
            sh3 = "Further Improvements"
            st.header(h1)
            st.subheader(sh1)
            st.write(summary)
            st.write(sh2)
            st.write(summary_rewrite)
            st.write(sh3)
            st.write(summary_suggest)
    
            #Educational Background
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_education_display},
                {"role": "user","content": segment}
                ],
                temperature = 0
            )
    
            education = response.choices[0]['message']['content']
            
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_education_rewrite},
                {"role": "user","content": education}
                ],
                temperature = 0
            )
    
            education_rewrite = response.choices[0]['message']['content']

            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_education_suggest},
                {"role": "user","content": education_rewrite}
                ],
                temperature = 0
            )
    
            education_suggest = response.choices[0]['message']['content']
            
            h1 ="Education"
            sh1 = "What you have written"
            sh2 = "What we suggest"
            sh3 = "Further Improvements"
            st.header(h1)
            st.subheader(sh1)
            st.write(education)
            st.write(sh2)
            st.write(education_rewrite)
            st.write(sh3)
            st.write(education_suggest)
    
            #Skills
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_skills_display},
                {"role": "user","content": segment}
                ],
                temperature = 0
            )
    
            skills = response.choices[0]['message']['content']
            
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_skills_rewrite},
                {"role": "user","content": skills}
                ],
                temperature = 0
            )
    
            skills_rewrite = response.choices[0]['message']['content']

            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_skills_suggest},
                {"role": "user","content": skills_rewrite}
                ],
                temperature = 0
            )
    
            skills_suggest = response.choices[0]['message']['content']
            
            h1 ="Skills"
            sh1 = "What you have written"
            sh2 = "What we suggest"
            sh3 = "Further Improvements"
            st.header(h1)
            st.subheader(sh1)
            st.write(skills)
            st.write(sh2)
            st.write(skills_rewrite)
            st.write(sh3)
            st.write(skills_suggest)
    
            #Extracurriculars
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_extra_display},
                {"role": "user","content": segment}
                ],
                temperature = 0
            )
    
            extra = response.choices[0]['message']['content']
            
            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_extra_rewrite},
                {"role": "user","content": extra}
                ],
                temperature = 0
            )
    
            extra_rewrite = response.choices[0]['message']['content']

            response = completion.create(
                model="gpt-3.5-turbo",
                messages=[
                { "role": "system","content": prompt_extra_suggest},
                {"role": "user","content": summary}
                ],
                temperature = 0
            )
    
            extra_suggest = response.choices[0]['message']['content']
            
            h1 ="Extracurriculars"
            sh1 = "What you have written"
            sh2 = "What we suggest"
            sh3 = "Further Improvements"
            st.header(h1)
            st.subheader(sh1)
            st.write(extra)
            st.write(sh2)
            st.write(extra_rewrite)
            st.write(sh3)
            st.write(extra_suggest)
