
# 1.	Write a program to create a simple calculator that performs addition, subtraction, multiplication, and division.
# 2.	Convert Celsius to Fahrenheit
# 3.	Prime Factorization
# 4.	GCD of the number.
# 5.	Print Floyd’s Triangle
#                           1
#                          2 3
#                         4 5 6
#                       7 8 9 10
#                     11 12 13 14 15

# 6. Number Pyramid
#                             1
#                            123
#                           12321
#                          1234321
#                         123454321
#  7 .Pattern
#                                   10101
#                                   10101
#                                   10101
#                                   10101
#                                   10101


# 1 Ans
# print("Select option:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# opt = input("Enter choice (1/2/3/4): ")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if opt == '1':
#     result = num1 + num2
#     print("Result:", result)
# elif opt == '2':
#     result = num1 - num2
#     print("Result:", result)
# elif opt == '3':
#     result = num1 * num2
#     print("Result:", result)
# elif opt == '4':
#     if num2 != 0:
#         result = num1 / num2
#         print("Result:", result)
# else:
#     print("Invalid input! Please select a valid opt.")

# 2 Ans
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)

# 4 Ans
# GCD of two numbers
# num1=3
# num2=36
# while num2 != 0:
#     num1, num2 = num2, num1 % num2

# print("GCD of numbers is:", num1)

# 5 Ans
#     1
#    2 3
#   4 5 6
#  7 8 9 10
#11 12 13 14 15

# n=7
# number=1
# for i in range(n):
#     for k in range(n-i):
#         print(" ", end="")
#     for j in range(i+1):
#         print(number,end=" ")
#         number+=1
#     print()

# 6 Ans
#       1
#      123
#     12321
#    1234321
#   123454321
# n=5
# for i in range(n):
#     for m in range(n-i):
#         print(" ", end="")   
#     for j in range(i+1):
#         print(j+1,end="")
#     for k in range(i):
#         print(i-k,end="")
#     print()


# 7 Ans
# n=7
# number=1
# for i in range(n):
#     for k in range(n):
#         print(" ", end="")
#     for j in range(1):
#         print(10,end="")
#     for j in range(1):
#         print(101,end="")
#     print()