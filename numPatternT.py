# n=int(input("Enter a number:-"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ") 
#     print()
 
# #  Enter a number:-5
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# m=int(input("Enter a number:-"))   
# for i in range(m):
#     for j in range(m+i):
#         if j<i:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()
    
# # Enter a number:-5
# # * * * * *
# #   * * * * *
# #     * * * * *
# #       * * * * *
# #         * * * * *

# # -----------Zero-One Triangle------------

# x=int(input("Enter a number:-"))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         if(i%2==0):
#             if j%2==0:
#                 print("1",end=" ")
#             else:
#                 print("0",end=" ")
#         else:
#             if j%2!=0:
#                 print("1",end=" ")
#             else:
#                 print("0",end=" ")
#     print()
            
# # Enter a number:-5
# # 1
# # 0 1
# # 1 0 1
# # 0 1 0 1
# # 1 0 1 0 1

# # -----------Number Increasing Pyramid------------  

# n=int(input("Enter a Number:-"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print(j,end=" ")
#     print()

# # Enter a Number:-4
# # 1 2 3 4
# # 2 3 4
# # 3 4
# # 4

# # -----------Number Triangular------------
  
# n=int(input("Enter a Number:-"))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         if (j<=i):
#             print(i,end=" ")
#         else:
#             print(" ",end="")
#     print()
    
# # Enter a Number:-5
# #     1
# #    2 2
# #   3 3 3
# #  4 4 4 4
# # 5 5 5 5 5

# # -----------Number Changing Pyramid------------

# n=int(input("Enter a Number of Rows:-"))
# c=0
# for i in range(1,n+1):
#     for j in range(i):
#         c+=1
#         print(c,end=" ")
#     print()

# # Enter a Number of Rows:-5
# # 1 
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # 11 12 13 14 15

n=int(input("Enter a Number of Rows:-"))
col=(n*2)-1
col_itr=0

for i in range(n-1,-1,-1):
    # print(i)
    c=(n-i)
    for j in range(col):
        
        if i>j :
            print(" ",end=" ")
        elif(j>n+col_itr):
            print(" ",end=" ")
            col_itr+=1
        elif j<=n-1:
            print(c,end=" ")
            c-=1
        else:
            if c==0:
                c+=2
                print(c,end=" ")
            else:
                c+=1
                print(c,end=" ")   
    print()
    
        
        


