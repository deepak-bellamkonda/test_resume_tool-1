prompt_segment = '''Please extract the contact information from the  resume content into sections: \
1. Name\
2. Email \
3. Address \
4. Phone number \
and dont include descriptions to any sections and the resume is : '''

prompt_currentrole_display = "Please extract only one current role or job position and also the company and the duration from the provided resume."

prompt_summary_display = "Please extract the summary section from the provided resume."
prompt_skills_display = "Please extract the skills mentioned in the provided  resume."
prompt_workex_display = '''Please extract the work experience details from the provided resume one by one. For each work experience, provide the role, company name, and duration.\

Work Experience 1:\
Role: [Insert Role 1]\
Company: [Insert Company 1]\
Duration: [Insert Duration 1]\
Work Experience 2:\
Role: [Insert Role 2]\
Company: [Insert Company 2]\
Duration: [Insert Duration 2] \
.
.
.
Work Experience n:\
Role: [Insert Role n]\
Company: [Insert Company n]\
Duration: [Insert Duration n] '''

prompt_education_display = '''Please extract the educational background details from the provided resume one by one. For each education entry, provide the degree, institute, duration, and grade.\
Education Entry 1:\
Degree: [Insert Degree 1]\
Institute: [Insert Institute 1]\
Duration: [Insert Duration 1]\
Grade: [Insert Grade 1]\
Education Entry 2:\
Degree: [Insert Degree 2]\
Institute: [Insert Institute 2]\
Duration: [Insert Duration 2]\
Grade: [Insert Grade 2]]\
.
.
.
Education Entry n:\
Degree: [Insert Degree n]\
Institute: [Insert Institute n]\
Duration: [Insert Duration n]\
Grade: [Insert Grade n]]\
'''
prompt_extra_display = "Extract the extracurricular activities from the above resume. Extracurricular activities are the activities not part of professional or educational activities. These are usually hobbies, and other activities done for fun. Limit to displaying only 5 activities if there are too many extracurriculars. Only show a heading for each extracurricular activity. If there are no such activities,display "No Extracurriculars" and ask the user to enter the activities in any of the following categories Cultural,Volunteer,Musical activities,Miscellaneous,Sports"
