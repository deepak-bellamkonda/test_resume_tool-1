from io import BytesIO
import base64
import streamlit as st 
import requests
from PyPDF2 import PdfReader
import openai
api_key = "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"
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
                     text += page.extract_text()

                st.write(text)

                #st.write(decoded_content)
            else:
                st.write("Error occured,please Try again!")
            
            list_of_prompts=["Look at the resume given. Then extract the following fields in the JSON Format from the resume :Role the person is currently working in, summary of their work experience, their educational background,their work experience in each role, their skills, and their extracurricular activities. Show each data under its relevant heading. The resume is : ",
                            "Examine the current role person is working in extracted above and identify if it is missing following data :Role Name, Current company, and Duration . If missing any detail, rewrite the current role using blanks for missing data .Only show the question asking for missing details. Don't show a description.",
                            "Extract the work summary/description from the above and display the following in a JSON Format :- 1. Work Description 2. Years of experience.if not ask the user to enter 3. Industries worked in.Then rephrase the 1st point above to include the years of experience, industries worked in,so that it showcases the following values : Personal Impact,Entrepreneurial Drive,Inclusive Leadership,Courageous Change, Problem Solving, Expertise. Do not repeat the values as they are, and it need not include all the values.Do not add any unknown information, do not repeat phrases. Limit the description to less than 50 words",
                            "Extract the educational background from the above in JSON Format and ask the users if any of the following missing entries Degree,Institution ,GPA/Percentage ,Year for each education are present. and don't give me any extra suggestions ",
                            "Extract the skills from the above resume and make sure that the skills are relevant for management consulting resumes. Remove the skills that are not relevant.Present in json format. If no skills match the description, ask the user to enter at least three skills. Limit the skills to 4 and each skill should not exceed 3 words.If skills are lacking, suggest new skills in JSON format.",
                            "Extract the extracurricular activities from the above resume. Extracurricular activities are the activities not part of professional or educational activities. These are usually hobbies, and other activities done for fun. Limit to displaying only 5 activities if there are too many extracurriculars. Only show a heading for each extracurricular activity. If there are no such activities,display '''No Extracurriculars''' and ask the user to enter the activities in any of the following categories Cultural,Volunteer,Musical activities,Miscellaneous,Sports" ]
          
            
            prompt_1=list_of_prompts[0] + text
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_1,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            output = response.choices[0].text.strip()
            c=1
            format="Resume Segementation for prompt :-"+str(c)
            st.header(format)
            st.write(output)
            prompt_2=list_of_prompts[1] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_2,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            c=2
            format="Resume Segementation for prompt :-"+str(c)
            st.header(format)
            st.write(outputs)
            #prompt 3
            prompt_3=list_of_prompts[2] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_3,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            c=3
            format="Resume Segementation for prompt :-"+str(c)
            st.header(format)
            st.write(outputs)
            prompt_4=list_of_prompts[3] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_4,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            c=4
            format="Resume Segementation for prompt :-"+str(c)
            st.header(format)
            st.write(outputs)
            prompt_5=list_of_prompts[4] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_5,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            c=5
            format="Resume Segementation for prompt :-"+str(c)
            st.header(format)
            st.write(outputs)
            prompt_6=list_of_prompts[5] + output
            response = openai.Completion.create(
                   engine="text-davinci-002",
                   prompt=prompt_6,
                   max_tokens=1867,  # You can adjust the number of tokens as needed
                   api_key=api_key
                   )
            outputs = response.choices[0].text.strip()
            c=6
            format="Resume Segementation for prompt :-"+str(c)
            st.header(format)
            st.write(outputs)



