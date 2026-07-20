from src.change_calc import change_calculator

def test_change_calc_returns_dict(): 
    input = 1
    result = change_calculator(input)
    assert isinstance(result, dict)

class TestOneCoinEach():
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

class TestMultipleCoins():
    def test_result_for_4p(self): 
        input = 4
        result = change_calculator(input)
        assert result == {'2':2}