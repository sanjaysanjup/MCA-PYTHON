class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return self.length+self.width

    
l=float(input("Enter length:"))
w=float(input("Enter Width :"))

rect1 = Rectangle(l,w)

rectp = rect.perimeter()
recta = rect.area()

print("Perimeter rect1:",rectp)
print("area rect1:",recta)

l2=float(input('Enter length '))
w2=float(input("ENTER Width :"))

rect2 = Rectangle(l2,w2)

rect2p = rect2.perimeter()
rect2a = rect2.area()

print("Perimeter rect1:",rect2p)
print("area rect1:",rect2a)

if(rect2p<rectp):
    print("Rectangle 1 is greater")
elif rect2p>rectp:
    print("Rectangle 2 is greater")
else:
    print("Both are same")














