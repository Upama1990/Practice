'''n=int(input("Enter a number"))
fact = 1
for i in range (1, n+1):
    fact = fact*i
print(fact)'''    
            
n=int(input("Enter a number"))

def fact(a):
    if (a<0):
        print("Error, Factorial of negative number does not exists")
    elif (a == 0):
        print("The fcatorial od 0 is 1")

    else:
        fact = 1
        for i in range(1, a +1):
            fact=fact*i
        return fact

print (fact(n))    
        
