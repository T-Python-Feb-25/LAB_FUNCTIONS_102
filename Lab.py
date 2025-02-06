def find_primes(num1:int, num2:int):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return print("The both must be number")
    z=range(num1,num2+1)
    for i in z:
        if  i==2 or i==3 or i==5 or i==7:
            print(i)
            
        elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
            continue
        else:
            print(i)

        
   
   
find_primes(25,50)
find_primes("ss",10) 
find_primes(1,"dd") 
find_primes("ss","dd") 
find_primes(1, 10)