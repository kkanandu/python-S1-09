sqr=lambda x:x*x
rect=lambda l,br:l*br
tri=lambda b,h:0.5*b*h

x=int(input("Enter the side of Square :"))
print(sqr(x))
l=int(input("Enter the length of rectangle :"))
br=int(input("Enter the breadth of rectangle :"))
print(rect(l,br))
b=float(input("Enter the base of triangle :"))
h=float(input("Enter the height of triangle :"))
print(tri(b,h))
