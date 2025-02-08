#the function to check if the number is a prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#to print the number if it's a prime 
def prime_numbers_between(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print (num)

# Take user inputs
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Get prime numbers in the range and print them
prime_numbers = prime_numbers_between(start, end)


'''
this is the first Python lab in the Course
Feb7, 2025
By Mohammed Albushaier
'''
