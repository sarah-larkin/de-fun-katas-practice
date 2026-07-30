
# def change_calculator(change_needed): 
#     """
#     Return the minimum number of UK coins required to make the given amount of change.

#     Args:
#         arg (int): total amount of change required in pence 

#     Returns:
#         dict[str, int] : coin values, quantities 

#     Raises: 
#         TypeError: If change_needed is not an int 
#         ValueError: If change_needed is negative 
#     """
#     coins_pennies = [50,20,10,5,2,1]
#     #coins_pennies.sort(reverse=True) #to ensure always largest number first - not necessary as fixed

#     remaining_amount = change_needed
#     result = {}

#     if not isinstance(change_needed, int): 
#         raise TypeError("Enter valid number")
    
#     if change_needed < 0: 
#         raise ValueError("Change cannot be negative")
    
#     for coin in coins_pennies: 
#         while remaining_amount >= coin:  
#             if str (coin) not in result: 
#                 result[str (coin)] = 1    #create key value pair in result dict
#             else: 
#                 result[str (coin)] += 1   #increase the counter if already exists
#             remaining_amount -= coin
#     return result      

            
"""  
Use the while loop to keep subtracting the same num repeatedly before moving 
on with the loop

>= coin (no longer looking to get to 0) 
If remaining_amount bigger or == coin then keep taking from that coin in the coins_pennies list

Use IF statements to validate inputs and raise the corresponding Exceptions 
(only use try/except if calling code that could fail)

check out .get()
dictionary.get(keyname, value)
keyname	- Required. The keyname of the item you want to return the value from
value	- Optional. A value to return if the specified key does not exist. Default value None
"""

#----------
# refactor
#----------

def change_calculator(change_needed): 
    """
    Return the minimum number of UK coins required to make the given amount of change.

    Args:
        arg (int): total amount of change required in pence 

    Returns:
        dict[str, int] : coin values, quantities 

    Raises: 
        TypeError: If change_needed is not an int 
        ValueError: If change_needed is negative 
    """
    coins_pennies = [50,20,10,5,2,1]
    remaining_amount = change_needed
    result = {}

    if not isinstance(change_needed, int): 
        raise TypeError("Enter valid number")
    
    if change_needed < 0: 
        raise ValueError("Change cannot be negative")
    
    for coin in coins_pennies: 
        while remaining_amount >= coin:  
            coin_key = str(coin)
            result[coin_key] = result.get(coin_key, 0) + 1 #assign the .get() value to the dict

            remaining_amount -= coin

    return result    

""" 
result.get(coin_key, 0) 

this will return the value fromt he result dict or if the coin_key does not yet
exists it will return the 0 as specified 

You add 1 to that value 

result[coin_key] = ...
This assigns the value back to the dict 
"""