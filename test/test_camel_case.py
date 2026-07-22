from src.camel_case import to_camel_case
import pytest

class TestForm: 
    def test_empty_str(self): 
        test_phrase = ""
        with pytest.raises(ValueError): 
            to_camel_case(test_phrase, True)
    
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
    def test_returns_upper_camel_case_for_single_word_when_true(self): 
        test_phrase = "hello"
        result = to_camel_case(test_phrase, True)
        assert result == "Hello"
    
    def test_returns_upper_camel_case_for_phrase_when_true(self): 
        test_phrase = "this sentence"
        result = to_camel_case(test_phrase, True)
        assert result == "ThisSentence"

    def test_returns_upper_camel_case_for_long_phrase_when_true(self): 
        test_phrase = "This Bigger strange Sentence"
        result = to_camel_case(test_phrase, True)
        assert result == "ThisBiggerStrangeSentence"

    def test_returns_upper_camel_case_When_additional_white_space_gaps(self): 
        test_phrase = "This    Bigger   strange        Sentence"
        result = to_camel_case(test_phrase, True)
        assert result == "ThisBiggerStrangeSentence"

    def test_returns_upper_camel_case_with_leading_trailing_white_space(self): 
        test_phrase = "      This bigger Strange sentence          "
        result = to_camel_case(test_phrase, True)
        assert result == "ThisBiggerStrangeSentence"
    
    def test_returns_upper_camel_case_for_single_word_when_false(self): 
        test_phrase = "hello"
        result = to_camel_case(test_phrase, False)
        assert result == "hello"

    def test_returns_lower_camel_case_for_phrase_when_false(self): 
        test_phrase = "this sentence"
        result = to_camel_case(test_phrase, False)
        assert result == "thisSentence"

    def test_returns_lower_camel_case_for_long_phrase_when_false(self): 
        test_phrase = "This Bigger strange Sentence"
        result = to_camel_case(test_phrase, False)
        assert result == "thisBiggerStrangeSentence"

    def test_return_camel_case_when_already_camel_case(self): 
        test_phrase_1 = "ThisSentence"
        result_1 = to_camel_case(test_phrase_1, False)

        test_phrase_2 = "thisSentence"
        result_2 = to_camel_case(test_phrase_2, True)

        assert result_1 == "thissentence"
        assert result_2 == "Thissentence"
        #func requires white space so will not work if already camel case 