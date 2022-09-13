student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇

def calculate_grades (score):
 if score <=100 and score >=91:
  return "Outstanding"
 elif score <= 90 and score >= 81:
  return "Exceeds Expectations"
 elif score <= 80 and score >= 71:
  return "Acceptable"
 else:
  return "Fail"

student_grades['Harry'] = calculate_grades(student_scores['Harry']) 
student_grades['Ron'] = calculate_grades(student_scores['Ron']) 
student_grades['Hermione'] = calculate_grades(student_scores['Hermione']) 
student_grades['Draco'] = calculate_grades(student_scores['Draco']) 
student_grades['Neville'] = calculate_grades(student_scores['Neville']) 
    

# 🚨 Don't change the code below 👇
print(student_grades)
