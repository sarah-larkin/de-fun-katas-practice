"""  
cash up the till the the end of the day
arg: dict
return str
"""

def till_add(till): 
    money = {
        "1p": 0.01,
        "2p": 0.02,
        "5p": 0.05,
        "10p": 0.1,
        "20p": 0.2,
        "50p": 0.5,
        "£1": 1.0,
        "£2": 2.0,
        "£5": 5.0,
        "£10": 10.0,
        "£20": 20.0,
        "£50": 50.0
        }
    
    total = 0 

    for key, value in till.items(): 
        total += money[key] * value
    print(total)

    if total < 1: 
        total = int(total * 100 )
        return str(total) + "p"
    
    if total > 1: 
        return "£" + str(total)




