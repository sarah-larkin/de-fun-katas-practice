from src.h_fold_string import fold_string

class TestFoldStringForm:
    def test_empty_string(self): 
        input = ""
        assert fold_string(input) == ""
    def test_output_is_string(self): 
        input = "code"
        assert isinstance(fold_string(input), str)

class TestFoldStringOutput:
    def test_one_even_count_word_inverted(self):
        input = "code"
        output = "oced"
        assert fold_string(input) == output
    def test_one_odd_count_word_inverted(self):
        input = "codes"
        output = "ocdse"
        assert fold_string(input) == output
    def test_longer_even_count_word_inverted(self):
        input = "abcdef"
        output = "cbafed"
        assert fold_string(input) == output
    def test_longer_odd_count_word_inverted(self):
        input = "Northcoders"
        output = "htroNcsredo"
        assert fold_string(input) == output
    def test_phrase_with_spaces(self): 
        input = "python is cool"
        output = "typnoh is oclo"
        assert fold_string(input) == output
