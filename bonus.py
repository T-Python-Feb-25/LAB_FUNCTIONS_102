def check(string:str) -> str: 
    ''' 
    This Function Returns A String With separation before capital letter and convert it to lower
    
    Args:
    string (str): The Phrase You Want to Sperate

    Return
    str: returns a string with separation based on capital letter and convert it to lower 
    '''
    result = ""
    if type(string) == str:
        for char in string:
            if char.upper() == char:
                result = result + " " + char.lower()
            else:
                result =  result + char 
    else: 
        return "It is not a string"
    return result.strip()



print(check("NawafAlahmadi"))