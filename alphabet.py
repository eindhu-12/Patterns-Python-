
#  -------------------------z Pattern-------------       

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
