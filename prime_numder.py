import math


def find_primes(first: int , second: int) ->None:

    for x in range(first, second + 1):
        if x > 1:
            check_prime = True
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i ==0:
                    check_prime =False 
                break

            
            if check_prime:
                print(x)
find_primes(10, 50)                
                

