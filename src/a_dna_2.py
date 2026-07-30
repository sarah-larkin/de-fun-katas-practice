
def dna_pairs(dna_str):
    result = []

    combinations = {"C": "G", "G": "C", "T": "A", "A":"T"}

    for letter in dna_str: 
        result.append([letter, combinations[letter]])

    return result


dna_pairs("C")