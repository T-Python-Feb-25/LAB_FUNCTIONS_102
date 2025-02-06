
x=input("Enter the first number: ")
y=input("Enter the second number: ")
def find_primes(x:int, y:int):
    
    'This function finds the prime numbers between x and y'
    for i in range(x,y+1):
        if i > 1:
            for n in range(2, i):
                if (i % n) == 0:
                    break
            else:
                    print(i)
    return i
find_primes(int(x), int(y))

print(find_primes.__doc__)
    