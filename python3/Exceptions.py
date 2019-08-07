students = {
    "first_name": "Thiago",
    "last_name": "Fonseca" 
}

try:
    print(students["nickname"])
except KeyError:
    print("Error finding the nickname")
except TypeError:
    print("Error finding the nickname")

try:
    print(students["nickname"])
except Exception as error:
    print(f"Error finding the nickname {error}")
