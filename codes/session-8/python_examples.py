# write a python program to print "Hello world"
print("Hello world")

# wrtie a python program to find the highest of two numbers
num_1 = 20
num_2 = 10
if num_1 > num_2:
	highest = num_1
else:
	highest = num_2
print(f"hightest: {hightest}")

# write a python program to find sum of two numbers
num_1 = 5
num_2 = 15
sum = num_1 + num_2
print(f"sum: {sum}")

# write a python program to assign a string value to a variable
python_string = "This is a string!"

# write a python program to find square root of a postive number
num = 8
num_sqrt = num ** 0.5
print(f"The square root of {num} is {num_sqrt}")

# write a python program to find the area of a triangle
side_1 = 5
side_2 = 6
side_3 = 7
s = (a + b +c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f"The area of the triangle is {area}")

# write a python program to multiply two numbers
num1 = 10
num2 = 15
multiplication = num1 * num2
print(f"Multiplication:{muliplication}")

# write a python program to find cube of a number
num = 10
cube = num ** 3
print(f"The cube of the number is: {cube}")

# write a python program to print natural numbers using for loop
num = 10
for i in range(1, num+1):
	print(i, end = " ")

# write a python program to print natural numbers in reverse order using while loop
num = 10
while(i >= 1):
	print(i, end = " ")
	i = i - 1

# write a python program to print the sum of first n natural numbers using for loop
n = 16
for value in range(1, n+1):
	total = total + value
print(f"total sum:{total}")

# write a python program to print the average of first n natural numbers using for loop
n = 15
for value in range(1, n+1):
	total = total + value
average = total/n
print(f"average: {average}")

# write a python program to print if a year is leap year using if statement
year = 1729
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
	print(f"{year} is leap year")
else:
	print(f"{year} is not a leap year")

# write a python program to print if a number is odd or even
num = 30
if(num % 2 == 0):
	print(f"num is even")
else:
	print(f"num is odd")

# write a python program to print even numbers from 1 to n using for loop
n = 30
for number in range(1, n+1):
	if(number % 2 == 0):
		print(f"{number}")

# write a python program to print odd numbers from 1 to n using for loop
n = 25
for number in range(1, n+1):
	if(number % 2 != 0):
		print(f"{number}")

# write a python program to print if a number is positive or negative
number = 31
if(number > 0):
	print(f"{number} is a positive number")
elif(number < 0):
	print(f"{number} is a negative number")
else:
	print("The number is zero")

# write a python program to print profit or loss using elif statement
actual_cost = 200
sale_amount = 300
if(actual_cost > sale_amount):
	amount = actual_cost - sale_amount
	print(f"total loss amount {amount}")
elif(sale_amount > actual_cost):
	amount = sale_amount - actual_cost
	print(f"total profit amount {amount}")
else:
	print("No profit, no loss.")

# write a python program to print square of a number
num = 25
square = num * num
print(f"the square of a given number is {square}")

# write a python program to find total, average and percentage of five subjects
english = 70
math = 80
computer = 88
physics = 87
history = 78
total = english + math + computer + physics + history
average = total / 5
percentage = (total / 500) * 100
print(f"total marks {total}")
print(f"average marks {average}")
print(f"marks percentage {percentage}")