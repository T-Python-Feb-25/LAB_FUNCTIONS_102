def cartstring(string:str):
    if not isinstance(string, str):
        print("Invalid input")
        return None
    result = " "
    for cahr in string:
        if cahr .isupper():
            result += " " + cahr.lower()
        else:
            result += cahr.lower()

    return result.strip()



input_string ="helloWorldThere "
outpot_string = cartstring(input_string)
print(outpot_string)