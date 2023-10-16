prompt_segment = '''Segment the given resume into appropriate headings and present in a json format.'''

prompt_currentrole_display = "Please extract the most recent/current role with the company and the duration from the json. Present it in a human readable format."

prompt_summary_display = "Please extract the summary section from the json. Display it in humand readable format. Make it less than 20 words."
prompt_summary_rewrite = "Rewrite the given work summary for a consulting resume. Use the McKinsey hiring values for reference, but do not use them directly. Make the sentence structure not repetitive. Limit to less than 20 words"
prompt_summary_suggest = "Look at the work summary and suggest 3 additional improvements that can be done."

prompt_skills_display = "Please extract the skills mentioned in the json."
prompt_skills_rewrite = "Extract the 4 skills that are relevant for a consulting resume. Only show the skills"
prompt_skills_suggest = "Suggest 3 additional skills that are similar to the skills mentioned and relevant for consulting."

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
prompt_workex_rewrite = ""
prompt_workex_suggest = ""

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
prompt_education_rewrite = "Rewrite the information given in a clean format suitable for consulting resume"
prompt_education_suggest = "Suggest some ideas on how to better write the given text in a consulting resume"

prompt_extra_display = "Extract the extracurricular activities from the json. Extracurricular activities are the activities not part of professional or educational activities. These are usually hobbies, and other activities done for fun. Limit to displaying only 5 activities if there are too many extracurriculars. Only show a heading for each extracurricular activity. If there are no such activities,display 'No Extracurriculars' and ask the user to enter the activities in any of the following categories Cultural,Volunteer,Musical activities,Miscellaneous,Sports"
prompt_extra_rewrite = "Select at max 4 activites from the given activites. Present them in a clean format for a consulting resume"
prompt_extra_suggest = "Suggest some extracurricular activities that are similar to the activities given and relevant for a consulting resume"
