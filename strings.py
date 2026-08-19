# Coding Exercise :
# Problem:
# You are given a string sentence . Print the characters at even indices.

a="Hello hi every one"
for i in range(0,len(a),2):
    print(a[i],end="")

# Problem:
# You are given a string s . Replace all spaces in the string with underscores ( _ )
# and print the modified string.

s = "Python is fun and powerful"
print(s.replace(" ","_"))

# Problem:
# You are given a string s . Check if the string contains only digits.

a="123456"
print(a.isdigit())

# You are given a string s . Print the string in reverse order.

s = "Python is amazing"
print(s[::-1])

# Problem:
# You are given a string s . Capitalize the first letter of each word in the string
# and print the modified string.

s = "python programming is fun"
print(s.title())


print("Welcome")