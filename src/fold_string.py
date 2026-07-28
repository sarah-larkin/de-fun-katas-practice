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

    mid_indx = len(phrase) // 2

    left = phrase[:mid_indx][::-1]      #reversed with slicing 
    middle = ""
    right = phrase[mid_indx:][::-1]

    if len(phrase) % 2:                 #if len(phrase) is odd number
        middle = phrase[mid_indx]
        right = phrase[mid_indx + 1:][::-1]

    return left + middle + right



    


