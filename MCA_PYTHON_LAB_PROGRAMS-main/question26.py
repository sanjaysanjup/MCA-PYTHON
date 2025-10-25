result = [] 
start = int(input("Enter the starting range (four-digit number): ")) 
end = int(input("Enter the ending range (four-digit number): ")) 
if start < 1000 or end > 9999 or start > end: 
    print("Invalid range. Please enter a valid four-digit range.") 
else: 
    for num in range(start, end + 1): 
        if num % 2 == 0: 
            root = int(num ** 0.5) 
            if root * root == num: 
                # check all digits even
                if all(int(d) % 2 == 0 for d in str(num)): 
                    result.append(num) 
print("Four-digit even perfect square numbers in the given range:") 
print(result)
