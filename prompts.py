prompt_segment = '''Segment the given resume into appropriate headings and present in a json format.'''

prompt_currentrole_display = "Please extract the most recent/current role with the company and the duration from the json. Present it in a human readable format."

prompt_summary_display = "Please extract the summary section from the json. Display it in humand readable format. Make it less than 20 words."
prompt_summary_rewrite = "Rewrite the given work summary for a consulting resume. Use the McKinsey hiring values for reference, but do not use them directly. Make the sentence structure not repetitive. Limit to less than 20 words"
prompt_summary_suggest = "Look at the work summary and suggest 3 additional improvements that can be done."

prompt_skills_display = "Please extract the skills mentioned in the json. Display them in csv format"
prompt_skills_rewrite = "Extract only 4 skills that are relevant for a consulting resume. Only show the skills"
prompt_skills_suggest = "Suggest pnly 3 additional skills that are similar to the skills mentioned and relevant for consulting."

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
prompt_workex_rewrite = "For each of the work experiences listed, analyze the description given then Rewrite the description by considering all the points given, and output just three points using the information in the description. The output points should include at least some values from the following : Personal Impact,Entrepreneurial Drive,Inclusive Leadership, Courageous Change, Problem Solving, Expertise. They should try to follow the framework of Action taken, stakeholders involved, and the impact on the metric. Show only the points without headings, and each point should not be more than 15 words. Add blanks for where relevant numbers can be added to show impact."
prompt_workex_suggest = "For each of the work experiences given, suggest how they can further improve the description. Show approach to calculate numbers where we have given then blanks in the description. "

prompt_education_display = '''Please extract the educational background details from the provided json. For each education entry, provide the degree, institute, duration, and grade.\
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
prompt_education_rewrite = "Rewrite the information given in a clean format suitable for consulting resume in Markdown."
prompt_education_suggest = "Give suggestions around including academic achievements and their types to improve the given information.Give only the suggestions in a paragraph in less than 30 words"

prompt_extra_display = "Extract only 3 extracurricular activities from the json that are relevant for a consultant. Extracurricular activities are the activities not part of professional or educational activities. These are usually hobbies, and other activities done for fun. If there are no such activities,display 'No Extracurriculars'"
prompt_extra_rewrite = "Rewrite 3 activities for a consulting resume. Suggest highlighting relevant achievements in each. Limit to less than 15 words each."
prompt_extra_suggest = "Suggest 2 extracurricular activities that are not included above which would be relevant for a consulting resume"
