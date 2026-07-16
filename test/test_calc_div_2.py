from src.calc_div_2 import calc_div
import pytest

#The challenge is to implement a function which adds all the 
# multiples of three and five below a certain number.

# class TestOutliers: #(original and refactor_1)
#     def test_non_num(self): 
#         assert calc_div("one") == "enter valid number"
#         assert calc_div([2]) == "enter valid number"
#         assert calc_div({2: 3}) == "enter valid number"
#         assert calc_div(True) == "enter valid number" #booleans are subclass of int
#     def test_no_arg(self): 
#         #None added as kwarg (refactor_1)
#         assert calc_div() == "enter valid number" 
#         assert calc_div(None) == "enter valid number"
    
class TestHappyPath: 
    def test_arg_below_3(self): 
        assert calc_div(0) == 0 
        assert calc_div(1) == 0 
        assert calc_div(2) == 0 
        assert calc_div(3) == 0 # question states below a number so here is not inclusive of 3
    
    def test_calc_div_output(self): 
        assert calc_div(10) == 23 
        assert calc_div(6) == 8
        assert calc_div(5) == 3
        assert calc_div(12) == 33
        assert calc_div(15) == 45
        assert calc_div(4) == 3

class TestExceptions:
    def test_exceptions(self):
        with pytest.raises(TypeError): 
            calc_div()
  
        with pytest.raises(TypeError): 
            calc_div("one")

        with pytest.raises(TypeError): 
            calc_div([2])
        

  