""" 
first attempt
"""

# def to_camel_case(phrase: str, case: bool):
    # """Convert sentence to upper or lower camel case 

    # Args: 
    #     arg (str) : sentence to convert to upper or lower camel case 
    #     arg (bool): True for UpperCamelCase, False for LowerCamelCase 
    
    # Returns: 
    #     str : sentence in upper or lower camel case 

    # Raises: 

    # """
    
    # if not isinstance(phrase, str):
    #     raise TypeError()
    
    # if not isinstance(case, bool) :
    #     raise TypeError()
    
    # if phrase: 
    #     if case == True: 
    #         split_phrase = phrase.split()
    #         capitalized_phrase = [word.capitalize() for word in split_phrase]
    #         upper_camel_case = "".join(capitalized_phrase)
    #         return upper_camel_case
    #     if case == False: 
    #         split_phrase = phrase.split()
    #         first_word = split_phrase[0].lower()  # str
    #         remaining_phrase = split_phrase[1:]   # list
    #         capitalized_phrase = [word.capitalize() for word in remaining_phrase]
    #         capitalized_phrase_joined = "".join(capitalized_phrase) # str
    #         combined_phrase = first_word + capitalized_phrase_joined 
    #         return combined_phrase
    # else: 
    #     return "phrase needed"
 
#------------
# refactor
#------------

def to_camel_case(phrase: str, case: bool):
    """Convert sentence to upper or lower camel case 

    Args: 
        arg (str) : sentence to convert to upper or lower camel case 
        arg (bool): True for UpperCamelCase, False for LowerCamelCase 
    
    Returns: 
        str : sentence in upper or lower camel case 

    Raises: 
        TypeError: If args are not str & bool
        ValueError: If str in empty

    """
    
    if not isinstance(phrase, str):
        raise TypeError("phrase must be a string")
    
    if not isinstance(case, bool) :
        raise TypeError("case must be a boolean")
    
    if phrase == "": 
        raise ValueError("phrase cannot be empty")
    
    split_phrase = phrase.split()  #avoids repeats
       
    if case: 
        return "".join(word.capitalize() for word in split_phrase)
    if not case: 
        first_word = split_phrase[0].lower()  # str
        remaining_phrase = split_phrase[1:]   # list
        capitalized_phrase = [word.capitalize() for word in remaining_phrase]
        capitalized_phrase_joined = "".join(capitalized_phrase) # str
        combined_phrase = first_word + capitalized_phrase_joined 
        return combined_phrase


def camel_to_english(phrase: str): 
    """Convert camel case phrase to normal English sentence ending in full stop

    Args: 
        arg (str) : camel case phrase to covert to a sentence 
    
    Returns: 
        str : Standard English Sentence 

    Raises: 
        TypeError: If args are not str
        ValueError: If str in empty

    """

    if not isinstance(phrase, str):
        raise TypeError("phrase must be a string")
       
    if not phrase: 
        raise ValueError("phrase cannot be empty")

    if phrase[-1] == ".": 
        phrase = phrase.strip(".") 

    result = [phrase[0]]  #list

    for letter in phrase[1:]: 
        if letter.isupper():
            result.append(" ")    #can use append with list 
        result.append(letter)     #append every letter 

    return "".join(result).capitalize() + "."   #join list into str 


""" 
capitalize() will capitalize the first letter in a phrase AND make all other characters
lower case. 

Strings are immutable
Concatinating the string in the loop creates a new stirng every iteration
Using a list can be more efficient 

string.strip(characters) -- will remove leading/trailing whitespace OR specified character

"""


