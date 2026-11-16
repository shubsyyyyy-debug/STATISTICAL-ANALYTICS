name = input("enter your name")
age = int(input("enter your age"))
marks = int(input("enter your marks")) 
print("Name of the student is",name)
print("Age of the student is",age)
if marks >= 0 and marks <= 100:
    print("Marks of the student is",marks)
elif marks < 0 or marks > 95:
    print("Marks of the student if we add 5 bonus marks is",marks+5)
else:
    print("Invalid marks entered")

number = int(input("enter your number"))
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

number = int(input("enter your number"))
total = 0
for i in range(1, number+1):
    total += i
print("The sum of numbers from 1 to", number, "is", total)
