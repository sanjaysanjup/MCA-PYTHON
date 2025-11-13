c = int(input("How many elements: ")) 
list1 = [] 
for i in range(c): 
    list1.append(int(input("Enter the element: "))) 
# remove even numbers safely by creating new list
list1 = [i for i in list1 if i % 2 != 0] 
print(list1)
