def find_primes(start:int,end:int):
    ''''print all prime numbers in the given range start to end inclusive  
        args:
            start(int):the starting number inclusive
            end(int):the ending number inclusive
        returns:
            none:this function dosent return anything
    '''
    found=True
    print(f"primes numbers between {start} and {end} are:")
    for x in range(start,end+1):
        if x==1:
            continue

        for y in range(1,x):
           
            if y==1:
                continue
            elif x%y==0:
                found=False
                break
        if found:
            print(x)
        found=True
    
find_primes(25,50)
