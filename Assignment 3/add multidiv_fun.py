#Write a function for basic math operations like add multiply substract divide and use this in your program
# , take 2 number input from user.


def add(a,b):
    print(f"sum of {a}+{b}={a+b}")


def sub(a,b):
    print(f"subtract of{a}+{b}={a-b}")


def multi(a,b):
    print(f"multiplication of {a}-{b}={a*b}")


def div(a,b):
    if b==0:
        print("Error as divided by zero")
    else:
        print(f"division of {a}/{b}={a/b}")


print("1.ADD \n"
      "2.SUBTRACT \n"
      "3.MULTIPLY \n"
      "4.DIVIDE \n")
x=int(input("Enter your choice:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if x==1:
    add(a,b)
elif x==2:
    sub(a,b)
elif x==3:
    multi(a,b)
elif x==4:
    div(a,b)
else:
    print("Wrong choice")
