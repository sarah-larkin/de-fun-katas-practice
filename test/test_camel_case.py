from src.camel_case import to_camel_case
import pytest

class TestForm: 
    def test_empty_str(self): 
        test_phrase = ""
        result = to_camel_case(test_phrase, True)
        assert result == "phrase needed" 
    
    def test_wrong_type_for_str_value(self): 
        test_phrase = 123
        with pytest.raises(TypeError): 
            to_camel_case(test_phrase, True)

    def test_wrong_type_for_bool_value(self): 
        test_phrase = "this sentence"
        with pytest.raises(TypeError): 
            to_camel_case(test_phrase, "True")

    def test_returns_str(self):
        test_phrase = "this sentence"
        result = to_camel_case(test_phrase, True)
        assert isinstance(result, str)

class TestOutput: 
    def test_returns_upper_camel_case_when_true(self): 
        test_phrase = "this sentence"
        result = to_camel_case(test_phrase, True)
        assert result == "ThisSentence"

    def test_returns_upper_camel_case_for_long_phrase_when_true(self): 
        test_phrase = "This Bigger strange Sentence"
        result = to_camel_case(test_phrase, True)
        assert result == "ThisBiggerStrangeSentence"

    def test_returns_lower_camel_case_when_false(self): 
        test_phrase = "this sentence"
        result = to_camel_case(test_phrase, False)
        assert result == "thisSentence"

    def test_returns_lower_camel_case_for_long_phrase_when_false(self): 
        test_phrase = "This Bigger strange Sentence"
        result = to_camel_case(test_phrase, False)
        assert result == "thisBiggerStrangeSentence"