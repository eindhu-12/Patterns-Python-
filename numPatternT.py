# -----------Number Increasing Pyramid------------

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
# -----------Rhombus Pattern------------

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

# -----------Zero-One Triangle------------

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

# -----------Number Increasing Reverse Pyramid------------  

n=int(input("Enter a Number:-"))
for i in range(n-1,-1,-1):
    for j in range(n):
        if i>=j:
            print(j+1,end=" ")
    print()

# Enter a Number:-4
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# -----------Number Triangular------------
  
n=int(input("Enter a Number:-"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if (j<=i):
            print(i,end=" ")
        else:
            print(" ",end="")
    print()
    
# Enter a Number:-5
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

# -----------Number Changing Pyramid------------

n=int(input("Enter Number of Rows:-"))
c=0
for i in range(1,n+1):
    for j in range(i):
        c+=1
        print(c,end=" ")
    print()

# Enter a Number of Rows:-5
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# -----------Palindrome Triangle------------

n=int(input("Enter a Number of Rows:-"))
col=(n*2)-1
col_itr=0

for i in range(n-1,-1,-1):
    c=(n-i)+1
    for j in range(col):
    
        if(i>j):
            print(" ",end=" ")
        elif(j<n):
            c-=1
            print(c,end=" ")
            
        else:
            if(j>(n-1)+i):
                c+=1
                print(c,end=" ")
                
    print()
    
#     Enter Number of Rows:-4
#       1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4


    # ----------or---------
    # c=n-i
    # for j in range(col):
    
    #     if(i>j):
    #         print(" ",end=" ")
    #     elif(j<n):
    #         print(c,end=" ")
    #         c-=1
    #     else:
    #         if(j>(n-1)+i):
    #             if c==0:
    #                 c+=2
    #                 print(c,end=" ")
    #             else:
    #                 c+=1
    #                 print(c,end=" ")
    # print()
    
        
# -----------Reversed Number Triangle Pattern------------

n=int(input("Enter number of rows:-"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<=j):
            print(j,end=" ")
        else:
            print(" ",end="")
    print()

# Enter number of rows:-4
# 1 2 3 4
#  2 3 4
#   3 4
#    4


# -----------Mirror Image Triangle Pattern------------

n=int(input("Enter a End Number:-"))
row=(n*2)-1
c=n
for i in range(1,row+1):
    c=n
    for j in range(1,n+1):
        if(i<=j):
            print(j,end=" ")
        elif i>n and row-i<j:
            print(j,end=" ")
        else:
            print(" ",end="")
        
    print()
# Enter a End Number:-4
# 1 2 3 4
#  2 3 4
#   3 4
#    4
#   3 4
#  2 3 4
# 1 2 3 4

# -----------Pascal's Triangle ------------


n=int(input("Enter number of rows:-"))
for i in range(1,n+1):
    c=0
    cnt=0
    half=i//2
    for j in range(n,0,-1):
        
        if(i>=j and i<=2):
            print(1,end=" ")
        elif(i%2==1 and i>=j):
            if(cnt<=half):
                print(c+1,end=" ")
                c+=1
                cnt+=1
            else:
                c-=1
                print(c,end=" ")
                cnt+=1
        elif(i%2==0 and i>=j):
            if(cnt<half):
                print(c+1,end=" ")
                c+=1
                cnt+=1
            else:
                
                print(c,end=" ")
                c-=1
                cnt+=1
        else:
            print(" ",end="")
    print()
    

# Enter number of rows:-5
#     1 
#    1 1 
#   1 2 1 
#  1 2 2 1 
# 1 2 3 2 1 