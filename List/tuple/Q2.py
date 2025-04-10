# Sort The marks
marks = []
for i in range(6):
    userMarks = int(input(f"Enter {i+1} User Marks: "))
    marks.append(userMarks)
    marks.sort()

print(marks)