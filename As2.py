"""a=int(input("Enter angle a:"))
b=int(input("Enter angle b:"))
c=int(input("Enter angle c:"))
if a==b==c:
    print("The triangle is equilateral!")
elif a==b!=c or a==c!=b or b==c!=a:
    print("The triangle is isosceles!")
elif a!=b and b!=c and a!=c:
    print("The triangle is  scalene!")
else:
    print("Please input a triangle.")"""
"""a=input("Enter the month: ")
list1=['1','3','5','7','8','10','12','january','march','may','july','august','october','december']
list2=['4','6','9','11','april','june','september','november']
if a in list1:
    print("{} has 31 days". format(a))
elif a in list2:
    print("{} has 30 days". format(a))
else:
    print("{} has 28 days normally, and 29 days in a leap year.". format(a))"""

"""a=input("Enter a character:")
print(type(a))
if type(a)==str:
    print("{} is part of the alphabet". format(a))
elif type(a)==int:
    print("{} is a number". format(a))
else:
    print("{} is part of the special character list". format(a))"""


a = input("Please Enter Your Own Character : ")

if((a >= 'a' and a <= 'z') or (a >= 'A' and ch <= 'Z')): 
    print("{} is part of the alphabet". format(a))
elif(a >= '0' and a <= '9'):
    print("{} is a number". format(a))
else:
    print("{} is part of the special character list". format(a))
