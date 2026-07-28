def fold_string(phrase): 
    """Function to turn a string insideout

    Args: 
        arg (str) :  string of any length (including strings with spaces)

    Returns: 
        str : Order of the words stays the same, each word is inside out 
            ie. the internal letters moved out and external letters moved the the centre.
    
    Raises: 
        TBC

    """

    split_phrase = phrase.split() 
    output = []

    for word in split_phrase: 
        mid_index = len(word) // 2

        left = word[:mid_index][::-1]      #reversed with slicing 
        middle = ""
        right = word[mid_index:][::-1]

        if len(word) % 2:                 #if len(word) is odd number
            middle = word[mid_index]
            right = word[mid_index + 1:][::-1]

        output.append(left + middle + right)

    return " ".join(output)



    


