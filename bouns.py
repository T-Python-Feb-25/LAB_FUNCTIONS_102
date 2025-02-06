def check(char:str):
    '''
    This function takes a continuous string and puts a space before each capital letter.

    args :
    char (str) : Take a sentence
    return:
    str = The sentence is returned with a space before the capital letters.
    '''
    word = ""
    if type(char) == str:
        for character in char:
            if character == character.upper():
                word += " " + character.lower()
            else:
                word += character
    else:
        return " the input not string"
    return word.strip()

print(check("helloWorldThere"))