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


        
# ----------------Square Filled Pattern----------------

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
            
# Enter a number:-7
# *
# * *
# * * *
# * * * *
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
# Enter a number:-7
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *

# ----------Triangle Star Pattern  ----------------     
   

n=int(input("Enter a number:-"))
for i in range(n-1,-1,-1):
    for j in range(n):
        if(i<=j):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()
    
# Enter a number:-5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# ---------------- Diamond Pattern----------------

n=int(input("Enter odd number:-"))
col=n//2
for i in range(n):
    for j in range(col,-1,-1):
        if(i<=col):
            if(i>=j):
                print("*",end=" ")
            else:
                print(" ",end="")
        else:
            if(n-i>j):
                print("*",end=" ")
            else:
                print(" ",end="")
    print()

# Enter odd number:-7
#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 

n=int(input("Enter odd number:-"))
for i in range(n):
    for j in range(n):
        if((i==0 or i==n-1) and j==n//2):
            print("*",end=" ")
        elif(i<=n//2):
            if(j>=n//2-i) and (j<=n//2+i):
                print("*",end="  ")
            else:
                print(" ",end=" ")
        else:
            if(j>=i-n//2) and (j<=n-i+(n//2)-1):
                 print("*",end="  ")
            else:
                print(" ",end=" ")
    print()
    

# Enter odd number:-5
#     *     
#   * * *   
# * * * * *
#   * * *
#     *

# ---------------- K Pattern----------------


n=int(input("Enter odd number:-"))
col=n//2
for i in range(n):
    for j in range(0,col+1):
        if(i<=j):
            print("*",end=" ")
        else:
            if(i-col>=j and i>col):
                # print("hi")
                print("*",end=" ")
    print()
    
    
# Enter odd number:-7
# * * * * 
# * * * 
# * * 
# * 
# * * 
# * * * 
# * * * * 
