def primen(x):
	n=0
	for i in range(1,x+1):
	    if x % i == 0:
	        n=n+1
	if n==2:
	    print("It prime number =",x) 
	else:
	    print("It not prime number =",x) 
