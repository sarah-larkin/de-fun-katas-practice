from src.till_add import till_add

def test_returns_string(): 
    result = till_add({ "1p": 1, "2p": 1 })
    assert isinstance(result, str)

def test_3p_addition(): 
    till = {"1p": 1,"2p": 1}
    result = till_add(till)
    assert result == "3p"

def test_38p_addition(): 
    till = { "1p": 1, "2p": 1, "5p": 1, "10p": 1, "20p": 1 }
    result = till_add(till)
    assert result == "38p"

def test_over_one_pound_addition(): 
    till = { "5p": 1, "10p": 1, "20p": 1, "50p": 1, "£1": 1 }
    result = till_add(till)
    assert result == "£1.85"

def test_value_above_one(): 
    till = { "1p": 2, "2p": 3 }
    result = till_add(till)
    assert result == "8p"