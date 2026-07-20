
def change_calculator(change_needed): 
    """calculates the coins needed for change using the smallest amount of change necessary

    Args:
        arg (int): total amount of change required in pence 
    """
    coins_pennies = [50,20,10,5,2,1]
    coins_pennies.sort(reverse=True) #to ensure always largest number first 


    remaining_amount = change_needed
    result = {}

    if change_needed < 100: 
        for num in coins_pennies: 
            if remaining_amount - num == 0:            #if only one coin required
                result[str(num)] = 1
                return result
            if remaining_amount - num > 0 : 
                remaining_amount -= num
                result[str(num)] = 1 
                # for num in coins_pennies: 
                #     if remaining_amount - num == 0: 
                #         result[str(num)] += 1
                #     if remaining_amount - num > 0:
                #         result[str(num)] += 1

                #don't nest loop, add other conditions 
    return result                      

    
    # return {}

change_calculator(3)