num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
  print(num1, "and", num2, "are not equal.", num1, "is greater than", num2)
  print(num1, "is the maximum number of both the numbers, and", num2, "is the minimum number of both the numbers.")
elif num1 < num2:
  print(num1, "and", num2, "are not equal.", num2, "is greater than", num1)
  print(num2, "is the maximum number of both the numbers, and", num1, "is the minimum number of both the numbers.")
else:
  print("Both", num1, "and", num2, "are equal.")