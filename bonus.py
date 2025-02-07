


def fix_case(lowercase_split: str) -> str:
    if not isinstance(lowercase_split, str):
        raise ValueError("Error: Input must be a string")
    
    new_string = ""

    for lettter in lowercase_split:
        if lettter.isupper():
            new_string += " " + lettter.lower()

        else:
            
            new_string += lettter

    return new_string.strip()
        
result = fix_case("HelloWorld")
print(result)       
         
    