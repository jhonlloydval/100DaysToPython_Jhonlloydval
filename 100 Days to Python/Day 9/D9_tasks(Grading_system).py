# DAY 9 TASK
# MAKING A SIMPLE GRADING SYSTEM USING DICTIONARY

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for score in student_scores:
    student_grades[score] = ""
    if student_scores[score] >= 91:
        student_grades[score] = "Outstanding"
    elif student_scores[score] >= 81:
        student_grades[score] = "Exceeds Expectations"
    elif student_scores[score] >= 71:
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

print(student_grades)
        
# NESTED DICTIONARY TASK

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# Printing "Lille"
print(travel_log["France"][1])

# Nested Lists
# Printing an index in a list inside a list 
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

for i in nested_list:
    print(i)

# Nested Dictionaries

travel_log2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visit": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}
print(travel_log2["Germany"]["num_times_visited"][2])