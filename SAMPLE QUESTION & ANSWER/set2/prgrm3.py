class number:
    def __init__(self,n,list1):
        self.n=n
        self.list1=list1
    def odd_numbers(self):
        return [num for num in self.list1 if num%2!=0]
    def not_divisible_by_3(self):
        return [num for num in self.list1 if num%7!=0]
list1=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print("list1:",list1)
numbers=number(n,list1)
list2=numbers.odd_numbers()
print("odd number is:",list2)
list3=numbers.not_divisible_by_3()
print("number is not divisible by 7:",list3)
