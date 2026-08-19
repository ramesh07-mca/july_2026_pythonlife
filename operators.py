#1.Write a Python program to calculate the area of a rectangle using the given
#formula: area = length * width . Take the values of length and width as inputs from
#the user.

a=int(input("length:"))  #input 5
b=int(input("width:"))   #input 2
area_triangle=a*b
print(area_triangle)  # Output:10

#2.Write a Python program to demonstrate incrementing and decrementing a variable

a=200
a+=1
print(a) #increment
b=100
b-=1
print(b) #decremenet

#3.Write a Python program to convert temperature from Celsius to Fahrenheit. The
#formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
#input from the user

celsius=int(input("temperature"))      #input=42^C
fahrenheit=(celsius* 9/5 ) +32
print(f"Fahrenheit={fahrenheit}^F")    #OUTPUT : 107.6^F

#4.Write a Python program to calculate the simple interest given the principal
# amount, rate, and time (in years).

p=int(input("amount"))       #10000
t=int(input("time"))         #1
r=int(input("rate"))         #2
simple_interest= p*t*r/100
print(simple_interest)        #Output ; 200.0

#5.Write a Python program to concatenate two strings and display the result. The
#strings should be taken as input from the user.

a=input()
b=input()
print(a+b)

#6.Write a Python program to convert a distance from kilometers to miles

kilometers = int(input("Kilometer"))  #10KM
print(kilometers/1.609)               #Output: 6.21 miles

#7. Create a program that takes user input for their name and age.
#Use formatted strings (f-strings) to print a message welcoming the user and
#stating their age.

name=input("name")
age=int(input("age"))
print(f"welcoming the user:{name} and age is {age} ")

#8.Create a list called numbers that contains integers from 1 to 10.


a=[1,2,3,4,5,6,7,8,9,10]
print(2 in a)         #True
print(15 not in a)
                      #True