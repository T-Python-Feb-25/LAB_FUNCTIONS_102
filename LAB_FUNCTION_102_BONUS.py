def is_string(x:str):
    '''This function takes a string as a parameter and seperate the word and replace all word to small letter'''
    phrase=""
    if type(x) == str:
        for i in x:
            if i.upper() == i:
                phrase = phrase + ' ' + i.lower()
            else:
                phrase = phrase + i
    else:
        return "Not string"
    return phrase.strip()

print(is_string("helloWorldThere"))

print(is_string.__doc__)
