#print("hi")
#print(1+2)
#print(4**4)

'''
This is a 
long comment
'''
# escape sequences / escaped characters

#print(" \" ")
#print("a new line \n this is a new line")
# creates a new line with the rest of the printed string

# print("enter your name")
# print ( "hello " + input("enter your name: ") ) # gets the users name and then returns it with hello 

#print ("hello " * int(input("enter a number: ")) ) # asks for a number from the user and repeats hello that many times 
#print ("You are " + str(2020 - int(input("What year where you born in? "))) + " years old" ) # asks the user for what year they are born in, coverts it to an integer, subtracts it from 2020 (this year), then converts back to a string to be concatonated and the displayed to the user
x = None # You have to assigm a value to variable, so if you would like to assign nothing use None

things = [ 0, 1.6, "hello", True] # In python you are able to include any type of variables in your array 
print (things[3])

year_of_birth = input("what year are you born in?") 
birthYear = int(year_of_birth)
print("You are " + str(2020- birthYear) + " years old") 

word = "dog"
print(type(word)) # prints out what type the variable is, n this case it is a string
print(word.upper()) # upper function converts the string to all upper case 

number = 16
print(number) 
print(type(number)) # variable is of int type 

def triple(word): # function triple retrns a word 3 times
    return word*3

name = triple("cat")
print(name)

clg = "class"
print(clg)
clg = clg[1:]
print(clg)
