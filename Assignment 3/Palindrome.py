# Write a program to check Palindrome Number

num=int(input("Enter the digit"))
a=num
rev=0

#reverse the num
while num != 0:
    temp = num % 10
    rev = rev * 10 + temp
    num = num // 10

t=(a is rev)
if t==True:
    print("Number is palindrome ")
else:
    print("number is not palindrome")




#Methord 2


# num=input("Enter your number")
# l=len(num)
# rev=num[::-1]
#
#
# if rev==num:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

