#1. Write a Python program that takes a list of numbers as input numbers = [25, 30,
# 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
# 100, stop adding numbers and print "Sum exceeded 100".

num=[22,13,24,32,21,34,5,23]
sum=0
i=0
while i<len(num):
    sum+=num[i]
    i+=1 
    if sum>100:
        break
print(sum)

#2. Write a Python script that uses a for loop to iterate through numbers from 1 to
# 600. Print only the odd numbers, skipping the even ones using the continue
# statement 

for i in range(1,601):
    if i%2==0:
        continue 
    print(i)

# 3.Write a Python script that checks if a number is even or odd. If the number is
# even, print "Even"; if odd, do nothing (use the pass statement).

num=int(input("enter the num"))
if num%2==0:
    print("Even")
else:
    pass 

# Write a Python script that iterates through a list of words. If the word is "break,"
# exit the loop using the break statement. If the word is "skip," skip the rest of the
# code for the current iteration using the continue statement. For any other word,
# print the word.

list_words=["rafhu","gani","hi","ghanu","naghu","mad","break","raju"]
for i in list_words:
    if i=="break":
        break 
    elif i=="skip":
        continue
    print(i)
    