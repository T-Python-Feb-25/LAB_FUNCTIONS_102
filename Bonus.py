#bonus
def split_words(sentence:str):
    """
    the function separates the words at any capital letter
    and replace it with a small letter
    param:
        sentence (str): The input string .
    Returns:
        none: The function prints the final string with spaces and small letters.
    """
    if isinstance(sentence, str):
        new = ""
        for i in sentence:
            if i.isupper():
                new += " "
                new += i.lower()
            else:
                new += i
        print(new)
    else:
        print("you must enter a string")


split_words("helloWorldThere")
