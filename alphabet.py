#  -------------------------E Pattern-------------       
print("E-Pattern")
n=9
for i in range(n):
    for j in range(n):
        if(j==0 or i==0 or i==n-1 or i==n//2):
            print("*",end=" ")
        
    print()


print()

#  -------------------------N Pattern-------------       
print("N-Pattern")
n=8
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 :
            print("*",end=" ")
        elif (i>0 or i>=n-2) and(i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print()
#  -------------------------Z Pattern-------------       

print("Z-Pattern")

c=8
for i in range(10-1,-1,-1):
    
    for j in range(10):
        if(i==0 or i==9):
            print("*",end=" ") 
        else:
            if(j==c):
                print("*",end=" ")
                c-=1
            else:
                print(" ",end=" ")
    print()
# * * * * * * * * * * 
#                 *
#               *
#             *
#           *
#         *
#       *
#     *
#   *
# * * * * * * * * * *


