students = {
    "first_name": "Thiago",
    "last_name": "Fonseca" 
}

print(students["first_name"])

print(students.get("nickname", "Unknow"))


students["first_name"] = "Joselito"

print(students["first_name"])



del students["first_name"]

print(students)