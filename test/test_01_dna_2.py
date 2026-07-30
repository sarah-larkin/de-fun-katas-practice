from src.dna_2 import dna_pairs


def test_empty_str_returns_empty_list(): 
    assert dna_pairs("") == []

def test_c_returns_C_G(): 
    assert dna_pairs("C") == [["C", "G"]]
    
def test_2_letter_combination(): 
    assert dna_pairs("AG") == [ ["A", "T"], ["G", "C"] ]

def test_every_combination(): 
    assert dna_pairs("ATCG") == [["A", "T"],["T","A"], ["C", "G"], ["G", "C"]]