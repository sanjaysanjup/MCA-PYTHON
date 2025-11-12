class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return self.length + self.breadth
    
len1 = float(input("Enter the length of rectangle 1:"))
bre1 = float(input("Enter bredth of the rectangle 1:"))

rect1 = Rectangle(len1,bre1)

rect1a = rect1.area()
rect1p = rect1.perimeter()

print("\nArea of Rectangle 1:", rect1a)
print("Perimeter of Rectangle 1:", rect1p)


len2 = float(input("\nEnter the length of rectangle 2:"))
bre2 = float(input("Enter the bredth of rectangle 2:"))

rect2 = Rectangle(len2,bre2)

rect2a = rect2.area()
rect2p = rect2.perimeter()


print("\nArea of Rectangle 2:", rect2a)
print("Perimeter of Rectangle 2:", rect2p)


if(rect2a<rect1a):
    print("\nRectangle 1 has greater area")
elif rect2a>rect1a:
    print("\nRectangle 2 has  greater area")
else:
    print("\nBoth are same")




