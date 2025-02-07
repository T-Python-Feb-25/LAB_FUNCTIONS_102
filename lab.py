def separate_text(text)-> str :
    result = ""
    for char in text:
        if char.isupper() and result:  
            result += " "  
        result += char.lower()  
    return result


text = "helloWorldThere"
result = separate_text(text)
print(result)