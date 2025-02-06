def change_string_format(old_string:str):

    if isinstance(old_string,str):
        new_string=""
        for char in old_string:
            if char.isupper():
                new_string+=" "+char.lower()
            else:
                new_string+=char
        return new_string
        

print(change_string_format("helloWorldThere"))
