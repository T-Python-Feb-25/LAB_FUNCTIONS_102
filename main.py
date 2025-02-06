def find_primes(first_parameter:int,second_parameter:int):
    for num in range(first_parameter, second_parameter):
        if num < 2:
            continue
        is_primes = True
        for i in range(2, num // 2, +1):
            if num % i == 0:
                is_primes = False
                break
        if is_primes:
            print(num)

find_primes(25, 50)
