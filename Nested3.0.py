"""x=122
for i in range(0,3):#i=0-->=1 etc.
    ch=chr(x)
    x=x-1
    for j in range(0,i+1):#j--->(0,1)--->j=0-->j(0,2)-->j=1 etc.
        print(ch,end=" ")
    print(" ")"""#Normal triangle
"""for i in range(0,3):#i=0-->=1 etc.
    for j in range(0,i+1):#j--->(0,1)--->j=0-->j(0,2)-->j=1 etc.
        if j%2==0:
            print("Hi",end=" ")
        else:
            print("Bye",end=" ")      
    print(" ")
for i in range(3,-1,-1):
    for j in range(0,i+1):#j--->(0,1)--->j=0-->j(0,2)-->j=1 etc.
        if j%2==0:
            print("Hi",end=" ")
        else:
            print("Bye",end=" ")      
    print(" ")"""
"""n=int(input("enter the value of n:"))
k=2*n-2
for i in range(0,5):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        if j%2==0:
            print("&",end=" ")
        else:
            print("*",end=" ")      
    print(" ")"""
"""for i in range(0,9,2):#i=0-->=1 etc
    for j in range(0,i+1):#j--->(0,1)--->j=0-->j(0,2)-->j=1 etc.
        print("*",end=" ")
    print(" ")
for i in range(9,-1,-2):
    for j in range(0,i+1):
        print("\t",end="*")"""
"""for i in range(3,-1,-1):
    for j in range(0,i+1):#j--->(0,1)--->j=0-->j(0,2)-->j=1 etc.
        if j%2==0:
            print("Hi",end=" ")
        else:
            print("Bye",end=" ")      
    print(" ")"""
n=9
k=2*n-2
for i in range(10,0,-2):
    for j in range(0,k):
        print(end=" ")
    k=k+1
    for j in range(0,i-1):
        if j%2==0:
            print("&",end=" ")
        else:
            print("*",end=" ")      
    print(" ")
