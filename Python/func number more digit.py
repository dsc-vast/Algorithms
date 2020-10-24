
#Two natural numbers. This function finds which one has more digits.
def kolvo(a,b):    
    x1=len(str(a))
    x2=len(str(b))
    if x1>x2:
        return(a)
    else:
        return(b)

