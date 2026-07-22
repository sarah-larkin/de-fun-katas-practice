
def to_camel_case(phrase: str, case: bool):
    """Convert sentence to upper or lower camel case 

    Args: 
        arg (str) : sentence to convert to upper or lower camel case 
        arg (bool): True for UpperCamelCase, False for LowerCamelCase 
    
    Returns: 
        str : sentence in upper or lower camel case 

    Raises: 


    """
    
    if not isinstance(phrase, str):
        raise TypeError()
    
    if not isinstance(case, bool) :
        raise TypeError()
    
    if phrase: 
        if case == True: 
            split_phrase = phrase.split()
            capitalized_phrase = [word.capitalize() for word in split_phrase]
            upper_camel_case = "".join(capitalized_phrase)
            return upper_camel_case
        if case == False: 
            split_phrase = phrase.split()
            first_word = split_phrase[0].lower()  # str
            remaining_phrase = split_phrase[1:]   # list
            capitalized_phrase = [word.capitalize() for word in remaining_phrase]
            capitalized_phrase_joined = "".join(capitalized_phrase) # str
            combined_phrase = first_word + capitalized_phrase_joined 
            return combined_phrase
    else: 
        return "phrase needed"
    
    
