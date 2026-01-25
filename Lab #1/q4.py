while(1):
  print("1. Add two numbers")
  print("2. Subtract two numbers")
  print("3. Exit")

  choice = int(input("\nEnter your choice: "))
  if(choice==3):
    break
  elif(choice==1):
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    print("Result: ",num1+num2)
  elif(choice==2):
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    print("\nResult: ", num1-num2)
  else:
    print("Invalid choice")
