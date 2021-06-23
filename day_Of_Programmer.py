def dayOfProgrammer(year):    
    if year < 1918: # julian calendar        
        if (year%4==0):# leap year
            return("12.09."+str(year))        
        else:
            return("13.09."+str(year))        
    elif (year > 1918): # Gregorian calendar        
        if (year%400==0) or (year%4==0 and year%100!=0) or (year%400==0): #leap year
            return("12.09."+str(year))        
        else:
            return("13.09."+str(year))            
    elif(year == 1918):
        return("26.09." + str(year))       
            
    
dayOfProgrammer(1918)   
