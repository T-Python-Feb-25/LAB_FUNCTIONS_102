def modify_string(input_str):
    if not input_str.isalpha():  # Step 1: Check if the input is a string containing only letters
        return "The input must be a string containing only letters!"
    
    result = ""  # the new string will be saved in this variable
    
    for char in input_str: # Step 2: Go through each character in the string using for loop
        if char.isupper(): 
            result += " " + char.lower()
        else:
            result += char  
    
    return result 

# Step 3: Ask the user to input a string
user_input = input("Enter a string: ")

# Step 4: Call the function with the user's input and print the result
modified_string = modify_string(user_input)

# Step 5: Print the modified string
print("Modified string:", modified_string)
