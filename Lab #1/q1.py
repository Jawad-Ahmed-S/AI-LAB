name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

print("Name: ",name)
if marks>=85:
  grade = 'A'
elif marks>=70:
  grade = 'B'
elif marks>=50:
  grade = 'C'
else:
  grade = 'Fail'

print("Grade: ",grade)