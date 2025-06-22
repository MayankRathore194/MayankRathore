# Input a number from user and find its factorial using for loop
n=int(input("Enter a number"))
f=1
for i in range(n,0,-1):

    print(i,"* ",end="")
    f=f*i
print(" ")
print(f)


