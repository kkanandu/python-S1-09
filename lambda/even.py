lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("List of Numbers :",lst)
even= list(filter(lambda n:n%2==0,lst))#Filtering Even numbers from list
print("List of even Numbers :",even)
odd=list(filter(lambda n:n%2==1,lst))#filtering Odd Numbers
print("List of Odd Numbers :",odd)
