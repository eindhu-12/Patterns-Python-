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


# ---------------- Hallow Hourglass Pattern----------------

n=int(input("Enter odd Number:-"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1):
            print("*",end=" ")
        else:
            if(i==j or j==((n-1)-i)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# Enter odd Number:-7
# * * * * * * *
#   *       *   
#     *   *
#       *
#     *   *
#   *       *
# * * * * * * *

