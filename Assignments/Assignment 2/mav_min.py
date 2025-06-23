# Write a  Python program to find the smallest number in a list.
# Write a  Python program to find the second greatest number in a list.
# Write a  Python program to find the second smallest number in a list.
l=input("Enter lisrt with space")
list=l.split()
for item in list:
    int(item)
print(list)



#max
m=list[0]
for i in list:
    if m<i:
        m=i
print(f"Maximum item is :{m}")

#min
n=list[0]
for k in list:
    if n>k:
        n=k
print(f"Minimun item is :{n}")


# second max
list.remove(m)
p=list[0]
for i in list:
    if p<i:
        p=i
print(f"Second largest item is :{p}")
list.append(m)


#second min
list.remove(n)
q=list[0]
for k in list:
    if q>k:
        q=k
print(f"Second min item is :{q}")
list.append(n)



