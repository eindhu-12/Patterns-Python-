n=int(input("Enter a number:-"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()
 
m=int(input("Enter a number:-"))   
for i in range(m):
    for j in range(m+i):
        if j<i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

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
            
    