
def find_primes(x:int ,y:int):
    """
       Finds and prints prime numbers between two given numbers.
       Args:
           x (int): The starting number.
           y (int): The ending number.
       Returns:
           None: This function prints prime numbers and does not return anything.
       """
    for n in range(x,y+1):
        if n > 1:
            for i in range(2,n):
                if n % i == 0:
                    break
            else:
                 print(n)


find_primes(25,50)








