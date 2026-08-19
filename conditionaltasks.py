#1. Write a Python program that takes a character as input and checks whether
# it is a vowel or not. Use the
# if-else statement.

num=input("enter the character")
vowel="aeiouAEIOU"
if num in vowel:
    print("vowel")
else:
    print("Not vowel")


# 2.Write a program that takes an age as input and classifies the person into
# one of the following age groups:
# Child: 0-12 years
# Teenager: 13-17 years
# Adult: 18-64 years
# Senior: 65 years and older

age=int(input("enter the age"))
if age>=0 and age<=12:
    print(f"{age} years child")
elif age>=13 and age<=17:
    print(f"{age} years Teenager")
elif age>=18 and age<=64:
    print(f"{age} years Adult")
else:
    print("Senior above 64 years")



# 3.Write a program that takes an integer as input and classifies it as positive,
# negative, or zero. Use the
# if-elif-else statement.
 
num=int(input("enter the num"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

# 4.Create a program that checks whether a given year is a leap year or not. A
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.

year=int(input("year"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")  
else:
    print(f"{year} is not leap year")

# 5.Build a simple calculator program that takes two numbers and an operator
# (+, -, *, /) as input and performs the corresponding operation.

num1=int(input("num1"))
num2=int(input("num2"))
operator=input("operator")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
else:
    print(num1/num2)

# 6.Rewrite the following code using the short-hand
# if statement:
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd"
x=8
print("even" if x%2==0 else "odd")

#7.Create a program that calculates the final price after applying a discount.
# The program should take the original price and the discount percentage as
# input.
original_price=int(input("original_price"))
discount=int(input("discount"))
result=(original_price*discount)/100
original_price-=result
print(f"final price after applying a discount is {original_price}")


#8.Write a program that calculates the Body Mass Index (BMI) using the
# formula: BMI = weight (kg) / (height (m))^2. The program should take
# weight and height as input 

weight=int(input("weigth"))
height=int(input("height"))
bmi=weight/(height**2)
print(bmi)