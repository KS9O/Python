# Nested Lists

classroom = []

# Loop 7 times
for i in range(7):
    classroom.append([])
    for students in range(1, 11):
        classroom[i].append(students)

print("classroom = ", classroom)


for outer in classroom:
    print(f"outer: {outer}")
    for inner in outer:
        print(f"\inner: {inner}")
        