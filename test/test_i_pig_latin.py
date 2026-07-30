from src.i_pig_latin import pig_latin
import pytest

class TestForm: 
    def test_empty_str(self): 
        test_phrase = ""
        with pytest.raises(ValueError): 
            pig_latin(test_phrase)
    def test_phrase_type_str(self): 
        test_phrase = 123
        with pytest.raises(TypeError): 
            pig_latin(test_phrase)
    def test_additional_white_space(self): 
        test_phrase = "    northcoders    "
        assert pig_latin(test_phrase) == "orthcodersnay"

class TestOutput: 
    def test_one_consonant_word(self): 
        assert pig_latin("northcoders") == "orthcodersnay"
    def test_double_consonant_word(self): 
        assert pig_latin("sheffield") == "effieldshay"
    def test_triple_consonant_word(self): 
        assert pig_latin("three") == "eethray"
    def test_vowel_word(self): 
        assert pig_latin("algorithm") == "algorithmway"
    def test_multi_word_phrase(self): 
        test_phrase = "keep on coding"
        assert pig_latin(test_phrase) == "eepkay onway odingcay"
    def test_capital_consonant_word(self): 
        assert pig_latin("Northcoders") == "orthcodersNay"
    def test_capital_vowel_word(self): 
        assert pig_latin("Apple") == "Appleway"
    def test_no_vowels(self):
        assert pig_latin("rhythm") == "mrhythay"
        assert pig_latin("sky") == "yskay"
    def test_single_letter(self):
        assert pig_latin("a") == "away"
