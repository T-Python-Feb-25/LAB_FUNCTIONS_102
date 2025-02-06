def find_prime(start:int,end:int): 
        for num in range(start,end+1):
          checkPrime = True
          for i in range(2,(num//2) + 1):
              if num % i == 0:
                  checkPrime = False
                  break
          if checkPrime:
              print(num)
              
find_prime(20,50)
    