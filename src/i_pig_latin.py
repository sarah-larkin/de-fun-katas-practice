import pytest 

def pig_latin(phrase): 
    """translate english str to pig latin.
    The first consonant (or consecutive consonants) of each word is moved to the end and 'ay' is added.
    If the word starts with a vowel, 'way' is appended to the end. 

    Args:
        phrase (str): english phrase 
    """
    #edge cases
    if not phrase: 
        raise ValueError("full phrase needed ")

    if not isinstance(phrase, str): 
        raise TypeError("phrase must be a string")
    
    
    #code: 

    vowels = ['a', 'e', 'i', 'o', 'u']
    split_phrase = phrase.split()
    output = []

    for word in split_phrase: 
        prefix = ""
        if word[0] in vowels: 
            pig_word = word + 'way'
            output.append(pig_word)
        else: 
            for letter in word: 
                if letter not in vowels: 
                    prefix += letter
                else: 
                    break
                pig_word = word[len(prefix):] + prefix + 'ay'
                print(pig_word)
            output.append(pig_word)

    result = " ".join(output) 
    return result


    #first attempt
       
    # for word in split_phrase: 
    #     if word[0] not in vowels and word[1] not in vowels: 
    #         pig_word = word[2:] + word[:2] + 'ay'
    #         output.append(pig_word)
    #     elif word[0] not in vowels and word[1] in vowels: 
    #         pig_word = word[1:] + word[0] + 'ay'
    #         output.append(pig_word)
    #     else: 
    #         pig_word = word + 'way'
    #         output.append(pig_word)


   





pig_latin("northcoders")
pig_latin("sheffield")
pig_latin("algorithm")
pig_latin("three")
pig_latin("keep on coding")