"""# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
"""

def text_separetor(text:str)->str:
    if not isinstance(text,str):
        return "Invalid input .. the input should be text"
    new_text=""
    for letter in text:
        if letter.islower():
            new_text+=letter
        else:
            new_text+=f" {letter.lower()}"     
    return new_text
     
print(text_separetor("helloWorldThere"))