"""  
cash up the till the the end of the day
arg: dict
return str
"""

# ----------------
# first attempt
# ----------------

# def till_add(till): 
#     money = {
#         "1p": 0.01,
#         "2p": 0.02,
#         "5p": 0.05,
#         "10p": 0.1,
#         "20p": 0.2,
#         "50p": 0.5,
#         "£1": 1.0,
#         "£2": 2.0,
#         "£5": 5.0,
#         "£10": 10.0,
#         "£20": 20.0,
#         "£50": 50.0
#         }
    
#     total = 0 

#     for key, value in till.items(): 
#         total += money[key] * value
#     print(total)
#     return "£" + str(total)
  
# # below format is not necessary 
#     # if total < 1: 
#     #     total = int(total * 100 )
#     #     return str(total) + "p" 
    
#     # if total > 1: 
#     #     return "£" + str(total)


#-------------
# refactor
# -----------

# def till_add(till): 
#     # best to avoid floats if possible for better accuracy
#     money = {
#         "1p": 1,
#         "2p": 2,
#         "5p": 5,
#         "10p": 10,
#         "20p": 20,
#         "50p": 50,
#         "£1": 100,
#         "£2": 200,
#         "£5": 500,
#         "£10": 1000,
#         "£20": 2000,
#         "£50": 5000
#         }

#     # total = 0 

#     # for key, value in till.items(): 
#     #     total += money[key] * value
#     # print(total)
#     # return f"£{total / 100:.2f}"

#     total = sum(money[key] * value for key, value in till.items())
#     return f"£{total / 100:.2f}"


#--------------
# alternative
#--------------

def till_add(till): 
    total = 0 

    for money, qty in till.items():
        if money.endswith("p"): 
            value = int(money[:-1])
        else: 
            value = int(money[1:]) * 100

        total += value * qty 

    return f"£{total / 100:.2f}"

# no fixed lookup table required, extract direct from info given
# no floats - convert to penny value then convert back to £