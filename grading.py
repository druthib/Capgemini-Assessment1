name=input("enter the student name")
marks_1=input("enter the marks of first subject")
marks_2=input("enter the marks of second subject")
marks_3=input("enter the marks of third subject")
marks_4=input("enter the marks of fourth subject")
marks_5=input("enter the marks of fifth subject")
totalMarksObtained=int(marks_1)+int(marks_2)+int(marks_3)+int(marks_4)+int(marks_5)
print(f'total marks of the student is:{totalMarksObtained}')
totalMarks=500
percentage=(totalMarksObtained/totalMarks)*100
print(f'the percentage of the student is:{percentage}')
if percentage>=90:
    print('Outstanding')
elif percentage>=80:
    print("Best")
elif percentage>=70:
    print("Can do better")
else:
    print("fail")