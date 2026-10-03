student = {
    "name": "Rahul",
    "python": 75,
    "javascript": 62,
    "html": 88
}

print("Student Name:", student["name"])

for subject, mark in student.items():
    if subject != "name":
        print(subject, ":", mark)