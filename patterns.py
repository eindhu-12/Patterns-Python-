# # ----------------Square Filled Pattern----------------

a=int(input("Enter a Number:-"))
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()
    
# Enter a Number:-5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# ----------------Square Hallow Pattern----------------
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

# ----------Rectangle Half Pyramid   ----------------        
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
# ----------------Reversed Right Half Pyramid  ----------------
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

# ----------------Left Half Pyramid  ----------------

n=int(input("Enter a Number:-"))
for i in range(n-1,-1,-1):
    for j in range(n):
        if(j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# Enter a Number:-5
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# ----------------Reversed Right Half Pyramid  ----------------

n=int(input("Enter a Number:-"))
for i in range(n):
    for j in range(n):
        if(j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Enter a Number:-5
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
        
# ---------------- Right Pascal's Triangle----------------
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

# ---------------- Left Pascal's Triangle ----------------

y=int(input("Enter a number:-"))  
for i in range(y):
    for j in range((y-1)//2,-1,-1):
        if(i<=y//2):
            if(j<=i):
                print("*",end=" ")
            else:
                print(" ",end=" ")  
        else:
            if j<=(y-1)-i:
                print("*",end=" ")
            else:
                print(" ",end=" ")            
            
            
    print()
           
# Enter a number:-6
#     *
#   * *
# * * *
# * * *
#   * *   
# Enter a number:-6
#     *
#   * *
# * * *
# * * *
#   * *
#     *  


# ----------------Rhombus Pattern ----------------
  
m=int(input("Enter a number:-"))   
for i in range(m):
    for j in range(m+i):
        if j<i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
    
# Enter a number:-5
# * * * * *
#   * * * * *
#     * * * * *
#       * * * * *
#         * * * * *


        