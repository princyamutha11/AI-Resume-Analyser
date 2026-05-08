
# AI Resume Analyzer



# Section 1 - Required Skills

required_skills = ["python", "sql", "java", "dsa", "communication"]



# Section 2 - User Input

print("===== AI Resume Analyzer =====")

resume_input = input("Enter your resume skills: ").lower()

resume_skills = resume_input.split()



# Section 3 - Skill Analysis


matched_skills = []
missing_skills = []

for skill in required_skills:

    if skill in resume_skills:
        matched_skills.append(skill)

    else:
        missing_skills.append(skill)



# Section 4 - Resume Score Calculation


score = (len(matched_skills) / len(required_skills)) * 100



# Section 5 - Resume Level Prediction


if score >= 80:
    level = "Excellent Resume"

elif score >= 60:
    level = "Good Resume"

elif score >= 40:
    level = "Average Resume"

else:
    level = "Needs Improvement"



# Section 6 - Recommended Role


if score >= 80:
    role = "Software Developer"

elif score >= 60:
    role = "Python Developer"

elif score >= 40:
    role = "Junior Programmer"

else:
    role = "Needs Skill Improvement"



# Section 7 - Output Display


print("\n===== Resume Analysis Result =====")

print("\nMatched Skills:")
for skill in matched_skills:
    print(skill, "✔")

print("\nMissing Skills:")
for skill in missing_skills:
    print(skill, "✘")

print("\nResume Score:", score, "%")

print("Resume Level:", level)

print("Recommended Role:", role)



# Section 8 - Suggestions

print("\nSuggestions:")

for skill in missing_skills:
    print("- Improve", skill)