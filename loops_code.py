# if condition:
#     statement

# age = 18
# if age <= 20:
#     print("You are eligible to vote")
# else:
#     print("not eligible")

# marks = 100

# maths = 100
# social = 100
# science = 75


# if marks >= 90:
#     print("Grade A")
# elif marks >=80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# else:
#     print("Fail")

# if maths >= 95:
#     print("Grade A")
# elif social >= 85:
#     print("Grade B")
# elif science >= 50:
#     print("Grade C")
# else:
#     print("Fail")

# age = 25
# citizen = True

# if age >= 18:
#     if citizen == True:
#         print("Eligible to vote")
#     else:
#         print("not a citizen")
# else:
#     print("under age")


# age = 20
# citizen = True

# if age <= 25:
#     if citizen == True:
#         print("eligible for vote")
#     else:
#         print("not a citizen")
# else:
#     print("under age")

# age = 20

# if age >=18: print("eligible") 

# age = 20 
# result = "Adult" if age >= 18 else "minor"
# print(result)

# age = 25
# result = "Adult" if age >=18 else "minor"
# print(result)

# age = 25
# salary = 30000

# if age >= 20 and salary >= 25000:
#     print("eligible")
# else:
#     print("not eligible")

# num = 10

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("odd number")


# num = 30

# if num % 2 != 0:
#     print("even number")
# else:
#     print("odd number")

# numbers = [1,2,3,4,5]
# result = [num for num in numbers if num % 2 != 0]
# print(result)

# find the largest two numbers

# a = 20
# b = 30

# if a > b == 0:
#     print("A is largest")
# else:
#     print("B is largest")


# a = 10
# b = 50
# c = 30

# if a > b and a > c:
#     print("A is largest")
# elif b > a and b > c:
#     print("B is largest")
# else:
#     print("C is largest")


# check positive, negative or zero

# num = -1

# if num > 0 :
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# check leap year

# year = 2024

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("not a leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("not a leap year")  

# year = 2024
# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0:
#     print("not a leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("not a leap year")

# year = 2024

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("leap year")
# else:
#     print("not a leap year")


# def check_leap_year(year):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0 ):
#         return "leap year"
#     else:
#         return "not a leap year"

# print(check_leap_year(2024))
# print(check_leap_year(1900))
# print(check_leap_year(2000))
# print(check_leap_year(2025))


# for variable in sequence:
#     statement

# for i in range(1,6):
#     print(i)


# for i in range(1,10):
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(2,11,2):
#     print(i)

# while condition:
#     statement

# i = 1

# while i <= 5:
#     print(i)
#     i = i+1

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)


# for i in range(1,6):
#     if i == 7:
#         break
#     print(i)

# for i in range(1,6):
#     if i == 5:
#         continue
#     print(i)

# for i in range(1,4):
#     if i == 3:
#         pass
#     print(i)
    
# Print numbers from 1 to 10

# for i in range(1,11):
#     print(i)

# # Sum of numbers from 1 to 10
# total = 0

# for i in range(1,11):
#     total = total + i
# print(total)


# # multiplication table
# num = 5

# for i in range(1,11):
#     print(num,"x",i,"=",num * i)

# # multiplication of 15 table
# num = 15
# for i in range(1,11):
#     print(num, "x",i,"=", num * i )

# factorial of a number
# num = 5
# fact = 1
# for i in range(1,num + 1):
#     fact = fact * i
# print(fact)

# # reverse a string using a loop
# text = "Python"
# reverse = "" 

# for char in text:
#     reverse = char + reverse
# print(reverse)


# count vowels in a string

# text = "Python Programming"
# count = 0

# for char in text:
#     if char in "aeiou":
#         count += 1

#     print(count)


# print even numbers 1 to 20

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)


# check factorial
# num = 5
# fact =1
# for i in range(1,num + 1):
#     fact = fact * i
# print(fact)


# # check prime numbers from 1 to 20
# num = 7

# if num <= 1:
#     print("not prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")


# # count vowels of string

# text = "Python Programming"
# count = 0 
# for char in text:
#     if char in 'aeiou':
#         count += 1

#     print(count)


# # print even numbers from 1 to 20
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# # check the prime number
# num = 7
# if num <= 1:
#     print("not a prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")


 











