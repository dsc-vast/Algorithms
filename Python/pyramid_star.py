#get input from user
n=int(input("Enter a number: "))
i=1
while(i<=n):
    j=1
    while(j<=n-i):
        print(" ", end = '')
        j+=1
    j=1
    while(j<=i):
        print("*", end = '')
        j+=1
    j=1
    while(j<i):
        print("*", end = '')
        j+=1
    i+=1
    print('')
