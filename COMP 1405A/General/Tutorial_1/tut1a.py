#  tutorial 1 Sample file

# welcome!
welcomeMessage = "Welcome to Age Calculation!"
print( welcomeMessage )


name = input("what is your name? ")
name = name.capitalize()
born = int(input("In what year where you born in, " + name + " ?"))
year = int(input("what is the current year?"))
age = year - born
print(name+ " must be " + str(age - 1) + " or " + str(age) + " years old ")



#print("input was   : " + name)
#print("lower case  : " + name.lower())
#print("upper case  : " + name.upper())
#print("capitalized : " + name.capitalize())