n=int(input("Enter a Number:-"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1):
            print("*",end=" ")
        else:
            if j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# Enter a Number:-5
# * * * * *
# *       *
# *       *
# *       *
# * * * * * 
            
m=int(input("Enter a number:-"))
for i in range(1,m+1):
    for j in range(i):
        print("*",end=" ")
    print()
    
# Enter a number:-5
# *
# * *
# * * *
# * * * *
# * * * * *

k=int(input("Enter a number:-"))
for i in range(k):
    for j in range(k-i):
        print("*",end=" ")
    print()

# Enter a number:-5
# * * * * *
# * * * *
# * * *
# * *
# *

x=int(input("Enter a number:-"))
for i in range(x):
    for j in range(x):
        if(i<x//2):
            if(j<=i):
                print("*",end=" ")
        else:
            if(j>=i):
                print("*",end=" ")
    print()
            
# Enter a number:-5
# *
# * *
# * * *
# * *
# *        