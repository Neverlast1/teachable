
students = []
studentMarks = []

i = bool(0)

while i == 0:
    studentNum = str(input("Please enter the Student Number: "))
    examMark = float(input("Please enter the student's Exam Mark (/150): "))
    assignMark = float(input("Please enter the student's Assignment Mark (/100): "))
    tuteMark = float(input("Please enter the student's Assessable Tutorial Mark (/10): "))

    examPercent = 70*(examMark/150)
    assignPerecent = 20*(assignMark/100)
    tutePercent = 10*(tuteMark/10)
    totalMark = examPercent + assignPerecent + tutePercent
    finalMark = round(totalMark)

    print(finalMark)

    students.append(studentNum)
    studentMarks.append(finalMark)

    if i == 0:

        cont = input("Would you like to Enter another Student's results? y/n: ")
        if cont == "n":
            i = 1

print("Student number" + "           " + "Final Mark")
for x, y in zip(students, studentMarks):
    print(str(x) + "                      " + str(y))

print("Program has Ended!")