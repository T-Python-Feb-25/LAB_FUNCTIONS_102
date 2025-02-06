#welcome message
print("welcome to our website to Prime numbers calculator")
#let user choose 2 number to calculate it , only positive nums
num1 = int(input("Enter your first number "))
num2 = int(input("Enter your sec number "))

#function to find the primes it accept two positive nums
def find_primes (num1:int , num2:int):    
    #print the message
    print("The Prime numbers in the range are: ")    
    #first loop for check between nums
    for number in range(num1, num2 + 1 ):
        #check if the nums bigger then 1 becouse the prime start from 2
        if number > 1 :
            #sec loop for check for prime if accept div by 2
            for i in range(2, int (number ** 0.5) + 1):
                if (number % i) == 0:
                    #if yes so the loop go to break
                    break
            else:     
             print(number)
            
find_primes(num1 , num2)            
