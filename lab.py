start = int(input("start of the interval: ")) 
end = int(input("end of the interval: "))

def find_primes(start,end):
    for num in range(start,end+1):
        if num > 1:  #1 and negative numbers aren't prime numbers
        
         for i in range(2,num):
             if num % i == 0:
                 break 
         else:
             print(num)
             
find_primes(start,end)
print(f"all prime numbers between {start} and {end} have been printed")