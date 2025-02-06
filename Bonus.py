def modified_string(x:str):
    if not isinstance(x, str):
        return "the type is not string" 
    new_x=" "
    for i in x:
        if i.isupper():
            new_x+= " "
            new_x+=i.lower()
        else:
            new_x+=i
        
           
    print(new_x)        
                        

modified_string("HelloWorld")
modified_string("WelcomeGhaida")



