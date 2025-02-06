def find_primes(start, end):
    if start < 2:
        start = 2
    for num in range(start, end + 1):
        is_prime = True
        for x in range(2,int(num ** 0.5)+ 1):
            if num % x == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

find_primes(25,50)
