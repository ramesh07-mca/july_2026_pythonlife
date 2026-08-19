#Zero divion error
# a=10
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError as e: 
#     print(e)   #division by zero
# # else:
# #     print(a+b)



#Value Error
# try:
#     a=int(input("Enter num_1:"))
#     b=int(input("Enter num_2:"))
# except ValueError as e:
#     print(e)
#     # Enter num_1:ter
#     # invalid literal for int() with base 10: 'ter'
# else:
#     print(a-b)


#__________Type Error_________

# try:
#     a="hi"-"hello"
# except TypeError as e:
#     print(e)
#     # unsupported operand type(s) for -: 'str' and 'str'
# else:
#     print(a) #support + operator



#_________FileNotFoundError_________

# try:
#     file=open("sample.txt",mode="r")
# except FileNotFoundError as e:
#     print(e)
#     # [Errno 2] No such file or directory: 'sample.txt'
# else:
#     obj=file.read()
#     print(obj) 

#__________Index Error___________
# a=[1,2,3,45]
# try:
#     print(a[7])
# except IndexError as e:
#     print(e)
#     # list index out of range


#________Key Error __________

# a={"name":"Ramesh","age": 23,}
# try:
#     print(a["b"])
# except KeyError as e:
#     print(e)    #KeyError: 'b'

#__________Attribute Error_________

# a=10
# try:
#     print(a.upper())
# except AttributeError as e:
#     print(a)
#     # 'int' object has no attribute 'upper'



#______________overflow Error_________ 

# a=4.1234668
# try:
#     print(a**100000000)
# except OverflowError as e:
#     print(e)
#     # (34, 'Result too large')

# ____________IO Error_________ 

# with open("sample.txt","r") as file:
#     content=file.read()

#_______Runtime Error________
def check_value(a):
    if a<-10:
        print(a)
check_value(-5)