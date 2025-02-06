def change_string_format(old_string:str):
    '''convert uppercase latter to lowercase letter and add space before the letter 
       args:
           old_string(string):the input string that will be formatted 
       return:
           str:the formatted string with uppercase letter turned to lowercase letters and space before the uppercase letter
    '''

    if isinstance(old_string,str):
        new_string=""
        for char in old_string:
            if char.isupper():
                new_string+=" "+char.lower()
            else:
                new_string+=char
        return new_string
        

print(change_string_format("helloWorldThere"))
