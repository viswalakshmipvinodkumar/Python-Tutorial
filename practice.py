#Write a program to display your name, age, and favorite color

# name = input("Enter your name:")
# age=int(input("Enter your age:"))
# color = input("Enter your favorite color:")

# print(f"my name is {name} i'm   {age}  old and your favorite color is {color}")

#Write a program that asks two numbers and prints their sum.

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# print("The sum is:", num1 + num2)
#Write a program that prints your college name 5 times.

# name = "cusat"

# for  in range(5):

#     print(name)

#Take two numbers from the user and print their sum, difference, product, and quotient.

# c = int(input("enter number:"))
# d = int(input("enter another number:"))

# print(f"sum is:{c +d}")

# print(f"difference is:{c - d}")
# print(f"product is:{c * d}")
# print(f"quotient is:{c / d}")

#Write a program to check if a number is even or odd.

# num = int(input("enter the number:"))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


#Write a program to find whether a number is positive, negative, or zero
#num = int(input("enter the number:"))

# if num  == 0:
#     print(f"{num} is zero")
# elif num > 0:
#     print(f"{num} is positive")
# else:
#     print(f"{num} is negative")

#Write a Python program that checks if a number is between 10 and 50 or equal to 100.
# num = int(input("enter the number:"))

# if (num > 10 and num < 50) or num  == 100:
#     print(f"{num} is conndition true")
# else:
#     print(f"{num} is condition false")
    
#find largest of two numbers

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# if num1 > num2:
#     print(f"{num1} is largest")
# else:
#     print(f"{num2} is largest")
     
#find a year is leap year or not

# year = int(input("enter the year:"))
# if (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")
 

#print multiplication table of a number

# num = int(input("enter the number:"))

# for i in range (1, 21):
#     print(f"{num} x {i} = {num * i}")

#firnd sum of n natrual numbers

# n = int(input("enter a number:"))
# sum = 0
# for i in range(0, n+1):
#     sum += i

# print(f"Sum of first {n} natural numbers is: {sum}")    

#prime number or not
# num = int(input("enter a number:"))
# i = 2
# limit =int( num / 2)
# while i <= limit:
#     if num % i == 0:
#         print(f"{num} is not prime")
#         break
#     i += 1
# else:
#     print(f"{num} is prime")

#pattern printing

# n = 1

# while n < 5:
#     print(n * "* ")
#     n += 1

# pryamid pattern

# i = 1
# limit = int(input("enter the number of rows:"))
# while i <= limit:
#     print(" " * (limit - i) + "* " * i)
#     i += 1

#count odd and even numbers in a list

# numl = input("enter the list:")
# num = [int(x) for x in numl.split(",")]

# l = len([num])
# even_count = 0
# odd_count = 0

# for i in range(l):
#     if num[i] % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1  
# print(f"even count is:{even_count}")
# print(f"odd count is:{odd_count}")


#login system usinng lists username and password
user_names = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]

name = input("enter your username:")

for u in user_names:
    if name == u:
        pwd = input("enter your password:")
        index = user_names.index(u)
        if pwd == passwords[index]:
            print("login successful")
        else:
            print("incorrect password")
        break
    else:
         print("username not found")