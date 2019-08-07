student_names = []
student_names = ["Thiago", "Simone", "Tania"]

print(student_names[1])
print(student_names[-1])

student_names.append("Marco")

print(student_names)


print("Marco" in student_names)

print(len(student_names))


del student_names[1]

print(student_names)

print(student_names[1:2])

for name in student_names:
    print(f"Student name is {name}")


for index in range(7, 10):
    print(f"My index is {index}")

for index in range(1, 10, 3):
    print(f"My index is {index}")

    
for index in range(1, 10, 3):
    print(f"My index is {index}")