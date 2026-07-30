#The challenge is to implement a function which adds all the 
# multiples of three and five below a certain number.

#initial attempt

# def calc_div(num=None): 
#     if type(num) != int or not num: 
#         return "enter valid number"
#     elif num < 3: 
#         return 0 
#     else: 
#         div = [number for number in range(3, num) if number % 3 == 0 or number % 5 == 0]
#         return sum(div)


#refactor_1

# def calc_div(num=None): 
#     if num is None: 
#         return "enter valid number"
#     if not isinstance(num, int) or isinstance(num, bool): 
#         return "enter valid number"
#     else: 
#         return sum(number for number in range(3, num) if number % 3 == 0 or number % 5 == 0)
#         #generator expression
#         #used range(3 onwards) so the <3 is not necessary


#refactor_2

def calc_div(num): 
    if not isinstance(num, int) or isinstance(num, bool): 
        raise TypeError("num must be an int")
    else: 
        return sum(number for number in range(3, num) if number % 3 == 0 or number % 5 == 0)
        #generator expression
        #used range(3 onwards) so the <3 is not necessary