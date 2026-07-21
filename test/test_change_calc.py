from src.change_calc import change_calculator
import pytest

class TestStructure:
    def test_change_calc_returns_dict(self): 
        input = 1
        result = change_calculator(input)
        assert isinstance(result, dict)
    def test_zero_change(self): 
        input = 0
        result = change_calculator(input)
        assert result == {}


class TestOneCoinEach:
    def test_result_for_one_penny(self): 
        input = 1
        result = change_calculator(input)
        assert result == {'1':1}
    def test_result_for_2p(self): 
        input = 2
        result = change_calculator(input)
        assert result == {'2':1}
    def test_result_for_3p(self): 
        input = 3
        result = change_calculator(input)
        assert result == {'2':1, '1':1}
    def test_result_for_7p(self): 
        input = 7
        result = change_calculator(input)
        assert result == {'5':1, '2':1}
    def test_result_for_13p(self): 
        input = 13
        result = change_calculator(input)
        assert result == {'10':1, '2':1, '1':1}

class TestMultipleCoins:
    def test_result_for_4p(self): 
        input = 4
        result = change_calculator(input)
        assert result == {'2':2}
    def test_result_for_40p(self): 
        input = 40
        result = change_calculator(input)
        assert result == {'20':2}
    def test_result_for_44p(self): 
        input = 44
        result = change_calculator(input)
        assert result == {'20':2, '2':2}
    def test_result_for_60p(self): 
        input = 60
        result = change_calculator(input)
        assert result == {'50':1, '10': 1}
    def test_result_for_99p(self): 
        input = 99
        result = change_calculator(input)
        assert result == {'50': 1,'20':2, '5':1, '2':2}
    def test_result_for_150p(self): 
        input = 150
        result = change_calculator(input)
        assert result == {'50': 3}

class TestExceptions: 
    def test_change_is_wrong_type(self): 
        with pytest.raises(TypeError):
            change_calculator("10")

    def test_no_change(self): 
        with pytest.raises(TypeError):
            change_calculator()
    #python raises this, not handled in code 
    
    def test_neg_change(self):
        with pytest.raises(ValueError):
            change_calculator(-5)