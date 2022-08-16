# Dictionaries-and-Lists-Present-Students-
#A function to correspond the list of students who are present in class

def students_present(dictionary):
    new_list = []
    for (students, value) in dictionary.items():
        if "Here" in value or "Present" in value:
            new_list.append(students)
    return new_list
            

student_list = {"David" : "Here", "Marguerite" : "Here",
                "Jackie": "", "Joshua": "Present",
                "Erica": "Here", "Daniel": ""}
print("Present students:", students_present(student_list))
