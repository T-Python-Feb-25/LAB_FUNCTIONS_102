def modify_string(input_str):
    if not isinstance(input_str, str):
        return "Error The input  not a string."
    
    result = ""
    for char in input_str:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char
    return result.strip()


output = modify_string("HelloWorldThere")
print(output)  
