def fibonacci(n):
    if (n <=1):
        return n
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))
n= int(input("ENTER NUMBER OF TERMS:"))
print("FIBONACCI SEQUENCE:")
for i in range(n):
    print(fibonacci(i))
