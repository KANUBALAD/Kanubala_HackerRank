def bonAppetit(bill, k, b):    
    del bill[k]
    anna_charge = sum(bill)//2    
    if anna_charge == b:
        print("Bon Appetit")        
    else:
        print(b- anna_charge)
        
