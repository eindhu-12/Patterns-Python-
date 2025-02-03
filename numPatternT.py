n=int(input("Enter a number:-"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()
 
#  Enter a number:-5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

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

x=int(input("Enter a number:-"))
for i in range(1,x+1):
    for j in range(1,i+1):
        if(i%2==0):
            if j%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            if j%2!=0:
                print("1",end=" ")
            else:
                print("0",end=" ")
    print()
            
# Enter a number:-5
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
    