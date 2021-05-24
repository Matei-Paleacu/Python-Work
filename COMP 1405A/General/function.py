import random, myFunction #allows me to acces the functions in my other doc also imports random function

x = 12
y = 4

check = myFunction.bigger(x,y) #uses on of the functions inside the doc I called 
print(check)

check = myFunction.smaller(x,y)

print(check)

x = random.randint(1,10) #selects a random number from 1 - 10
print(x)

