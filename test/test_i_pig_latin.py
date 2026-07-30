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
        test_phrase = "northcoders"
        assert pig_latin(test_phrase) == "orthcodersnay"
    def test_double_consonant_word(self): 
        test_phrase = "sheffield"
        assert pig_latin(test_phrase) == "effieldshay"
    def test_triple_consonant_word(self): 
        test_phrase = "three"
        assert pig_latin(test_phrase) == "eethray"
    def test_vowel_word(self): 
        test_phrase = "algorithm"
        assert pig_latin(test_phrase) == "algorithmway"
    def test_multi_word_phrase(self): 
        test_phrase = "keep on coding"
        assert pig_latin(test_phrase) == "eepkay onway odingcay"