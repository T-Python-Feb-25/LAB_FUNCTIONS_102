#function accpet two num most be positive num
def parameter(x: int) -> int:
    #empty list fpr save even num
    even_num = []
    #variable ready by 0 num for 
    total = 0 
    #for loob start 2 end at x + 1 for even num , move 2 step for even num
    for number in range(2, x + 1, 2): 
        #add even num to var even_num
        even_num.append(number)
        #add num to total for calculate total  
        total += number 
        #print the nums in one line 
    print(f"The even numbers between 1 and {x} are: {', '.join(map(str, even_num))}")
    return total 

n = int(input("Enter a positive integer: "))
if n > 0: 
    print(f"The sum of even numbers between 1 and {n} is {parameter(n)}.")
else: 
    print("Please enter a positive integer.")
