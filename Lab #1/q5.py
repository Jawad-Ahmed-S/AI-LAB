Marks = [21,43,65,6]
def calculate_Averge(marks):
  sum=0
  for i in range(len(marks)):
    sum= sum+marks[i]
  return sum/len(marks)

avg = calculate_Averge(Marks)
print("Average: ",avg)