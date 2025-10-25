n = int(input("ENTER NUMBER OF N TERMS:")) 
if n <= 0: 
    print("Fibonacci series up to", n, "is not defined.") 
else: 
    first = 0 
    second = 1 
    print("The first", n, "numbers in the Fibonacci Series =") 
    if n == 1: 
        print(first) 
    else: 
        print(first, end="") 
        print(", ", second, end="") 
        for i in range(2, n): 
            fib = first + second 
            first = second 
            second = fib 
            print(", ", fib, end="") 
        print()
