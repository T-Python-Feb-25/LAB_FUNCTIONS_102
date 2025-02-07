def find_primes(number1:int, number2:int)-> int:
    for num in range(number1, number2):
        if num < 2:
            continue
        prime = True
        for i in range(2, int(num**0.5) + 1): # i seach the web for this
            if num % i == 0:
              prime = False
        if prime :
            print(num) 


print(find_primes(25, 50)) 

'''''
r = 4
v = 29
for r in range(r, v, +1):
    if r < 2  :
        r+= 1
        print(r)


'''''
'''''
num =10
for i in range(2, num):
    if num % i == 0:
        print("not pime")
        break
else:
    print("prime")
 
 '''''