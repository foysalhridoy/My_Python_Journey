a = int(input("Enter your age: "))
print("Your age is:",a)

# Conditional statement
# <, >, <=, >=, !=, ==
print(a<18)
print(a>18)
print(a==18)
print(a!=18)
print(a==18)
print(a<=18)
print(a>=18)

if(a>18):
    print("You can drive")
else:
    print("You can not drive")  


# ifelse
applePrice = 210
budget = 200

if (applePrice <= budget):
    print("Give me 1 kg apple")

else:
    print("I do not need apple")
   
    
# elif
applePrice  =10
budget = 200
if (budget - applePrice > 50):
    print("Give the apples")
    
elif(budget - applePrice > 70):
    print("Okay you can buy")
    
else:
    print("No thanks")                


# elif
num = int(input("Enter any number: "))
if(num < 0):
    print("The number is negative")
elif(num == 0):
    print("The number is zero")
elif(num == 999):
    print("The number is special")
else:
    print("The number is positive")   


#Nestedif
num = int(input("Enter any number: "))
if(num < 0):
    print("The number is negative")
elif(num > 0):
    if(num <= 10):
        print("The number is between 1-10")
    elif(num > 10 and num <= 20):
        print("The number is between 11-20")
    else:
        print("The number is greater than 20")
else:
    print("The number is zero")                
        
