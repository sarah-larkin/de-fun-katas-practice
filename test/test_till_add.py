from src.till_add import till_add

def test_returns_string(): 
    result = till_add({ "1p": 1, "2p": 1 })
    assert isinstance(result, str)

def test_3p_addition(): 
    till = {"1p": 1,"2p": 1}
    result = till_add(till)
    assert result == "3p"