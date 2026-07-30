import pytest 

def pig_latin(phrase): 
    """translate english str to pig latin.
    The first consonant (or consecutive consonants) of each word is moved to the end and 'ay' is added.
    If the word starts with a vowel, 'way' is appended to the end. 

    Args:
        phrase (str): english phrase 
    """
    #edge cases
    if not isinstance(phrase, str): 
        raise TypeError("phrase must be a string")
    
    if not phrase: 
        raise ValueError("full phrase needed ")
    
    #code: 
    vowels = {'a', 'e', 'i', 'o', 'u'} # set
    split_phrase = phrase.split()
    output = []

    # find the index of first vowel (don't have to create the temp prefix)
    for word in split_phrase: 
        if word[0].lower() in vowels: #use .lower to account for capitals 
            pig_word = word + 'way'
        else: 
            for i, letter in enumerate(word): #loop to find index of first vowel 
                if letter.lower() in vowels: 
                    pig_word = word[i:] + word[:i] + "ay"
                    break
            else:   #if no vowels (in for loop, not if/else statement so not created for every consonant found)
                pig_word = word[-1] + word[:-1] + "ay"
        output.append(pig_word)
    return " ".join(output)
    
