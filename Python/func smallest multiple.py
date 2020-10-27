#The natural numbers a and b. This function finds their smallest common multiple.
def NOK(a,b):   
    for i in range(1,(a*b)+1):
        if i%a==0 and i%b==0:
            break
    return(i)



