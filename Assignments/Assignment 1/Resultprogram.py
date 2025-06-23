#Enter student name,5 subject marks ,show percentage,total marks
#Display a result with name and percentage
name=input("Enter student name")
eng=int(input("Enter english marks"))
hindi=int(input("Enter hindi marks"))
physics=int(input("Enter physics marks"))
maths=int(input("Enter maths marks"))
chemistry=int(input("Enter chemistry marks"))
t=hindi+eng+physics+maths+chemistry
p=(t/500)*100
a=p
print("Name of the student:",name)
print("Total marks scored:",t)
print("Percentage:",p)