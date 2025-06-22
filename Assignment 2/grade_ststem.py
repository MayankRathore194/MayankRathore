# In your last program where you find the total and percentage of a student's marks of 5 subject,
# find the grade of the student using conditional statement.
# Eg. grade 'A' if percentage is greator than or equals to 60,
# 'B' for  percentage is greator than or equals to 50 and less than 60,
# 'C' for  percentage is greator than or equals to 40 and less than 50,
# 'D' for  percentage is greator than or equals to 33 and less than 40,
# otherwise 'Fail'
name=input("Enter student name")
eng=int(input("Enter english marks"))
hindi=int(input("Enter hindi marks"))
physics=int(input("Enter physics marks"))
maths=int(input("Enter maths marks"))
chemistry=int(input("Enter chemistry marks"))
t=hindi+eng+physics+maths+chemistry
p=(t/500)*100
print("Total marks:",t)
a=p
print("Name of the student:",name)
print("Total marks scored:",t)
if a>=50 and a<60:
    print("Grade is:A")
elif a>=40 and a<50:
    print("Grade is:B")
elif a>=33 and a<40:
    print("Grade is:C ")
else:
    print("fail")


print("Percentage:",p)