# 1.Write a Python program that calculates and prints the sum of the squares of
# numbers from 1 to 5 using a
# for loop.

sum=0
for i in range(1,6):
    re=i**2
    sum+=re 
print(f"sum of the squaresof 1 to 5 is {sum}")

# 2.Write a Python program that uses a
# while loop to print a countdown from 5 to 1.

number=5
while number>=1:
    print(number)
    number-=1

# 3.Write a Python program to print the multiplication table for a user-specified
# number using a nested for loop.

a=int(input("enter the number"))
for i in range(1,11):
    for j in range(1):
        print(f"{a}X{i}={a*i}")

# 4.Write a Python program that uses a "for" loop to find the sum of all even
# numbers between 0 and 10 (inclusive).
sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i
print(sum)

# 5.Calculate the sum of all numbers from 1 to a given number

a=int(input("enter the number"))
sum=0
for i in range(1,a+1):
    sum+=i 
print(sum)

# 6.Display numbers from a list using loop 

a=[2,5,7,90,23,2,56]
for i in a:
    print(i) 

# 7.Display numbers from -10 to -1 using for loop
a=-10
while a<=-1:
    print(a)
    a+=1

# 8.Write a Python program to print the cube of all numbers from 1 to a given
# number

a=int(input("enter the number:"))
for i in range(1,a+1):
    print(i**3)





    