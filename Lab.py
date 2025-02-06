def find_primes (num1:int , num2:int):
    '''
    This function takes two numbers and displays all the prime numbers between them.

    args:
    num1 (int) : prime number limit start
    num2 (int) : prime number limmt end
    return:
    int : all prime numbers between num1 and num 2
    '''
    for number in range(num1,num2+1):
        if number < 2:
            continue

        for i in range(2,number):
            if number % i == 0:
                break
        else:
            print(number)

find_primes(25,50)