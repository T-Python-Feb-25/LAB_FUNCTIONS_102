
def separates_by_capital(string:str):
    result = ""
    if not isinstance(string,str):
        print("input is not string. ")
        return None
    for char in string:
        if char.isupper():
            if char.index() == 0:
                result += str(char.lower())
            else:
                result += " " + str(char.lower())
        else:
            result += char
            
    
    
    return result

print(separates_by_capital("hello world there"))