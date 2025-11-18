class Rectangle:
    def __init__(self):
        self.length=0
        self.breadth=0
    def set_values(self):
        self.__length=float(input("Enter the length of the rectangle: "))
        self.__breadth=float(input("Enter the breadth of the rectangle: "))
    def area(self):
            return self.__length*self.__breadth
    def __lt__(self,other):
        return self.area()<other.area()
rect1=Rectangle()
print("Enter details of Rectangle 1: ")
rect1.set_values()
rect2=Rectangle()
print("\nEnter the values of Rectangle 2 ")
rect2.set_values()
if rect1<rect2 :
    print("\n\nArea of Rectangle 1 is smaller than Rectangle 2")
elif rect1>rect2 :
    print("\n\nArea of Rectangle 1 is greater than Rectangle 2")
else:
    print("\n\nArea of Both Rectangles are same")

        
