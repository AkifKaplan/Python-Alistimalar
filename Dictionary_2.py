students = {}

student_id1 = input("Enter student ID: ")
name1 = input("Enter student name: ")
surname1 = input("Enter student surname: ")
department1 = input("Enter student department: ")

students[student_id1] = {
    "name": name1,
    "surname": surname1,
    "department": department1
}

student_id2 = input("Enter student ID: ")
name2 = input("Enter student name: ")
surname2 = input("Enter student surname: ")
department2 = input("Enter student department: ")

students[student_id2] = {
    "name": name2,
    "surname": surname2,
    "department": department2
}

# Ask ID 
search_id = input("Enter a student ID to display their information: ")

print("Student ID:", search_id)
print("Name:", students[search_id]["name"])
print("Surname:", students[search_id]["surname"])
print("Department:", students[search_id]["department"])

