def find_prime(num1:int, num2:int) -> int:
    for num in range(num1, num2+1):
        if num > 1:
            prime = True
            for i in range(2,num):
                if num % i == 0:
                    prime = False
                    break
            if prime == True:
                print(num)
                
            
        
find_prime(1,50)

