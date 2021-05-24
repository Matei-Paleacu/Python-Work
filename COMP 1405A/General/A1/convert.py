import convertF

name = input("Please enter your name: ")
name = name.capitalize()
print("Hello " + name + " welcome to your personal unit converter.")
print()
print("Please choose which conversion you would like to preform: ")
print("1 - convert cm to m \n2 - convert percent to letter grade \n3 - convert L to ml \n4 - convert grams to kilograms \n5 - convert celcius to kelvin \n6 - convert yards to feet")
print()
choice = float(input("Choice:")) 

if choice == 1:
    cm =float(input("Value in cm to convert: "))
    meters = convertF.cmToM(cm)
    print( str(cm) + " cm = " + str(meters) + " meters")
    print()
    print("Goodbye " + name)
    exit()
else :
    if choice == 2:
        percent = float(input("Percent to conver to letter grade: "))
        letterGrade = convertF.pToLetter(percent)
        print(str(percent) + "% = " + letterGrade)
        print()
        print("Goodbye " + name)
        exit()
    else:
        if choice == 3:
            liter = float(input("Value of L to convert: "))
            milliliter = convertF.LtoMl(liter)
            print(str(liter) + " L = " + str(milliliter) + " milliliter")
            print()
            print("Goodbye " + name)
            exit()
        else:
            if choice == 4:
                grams = float(input("Value of g to convert: "))
                kilograms = convertF.gToKg(grams)
                print(str(grams) + " g = " + str(kilograms) + " Kg") 
                print()
                print("Goodbye " + name)
                exit()
            else:
                if choice == 5:
                    celcius = float(input("Value of celcius to convert: "))
                    kelvin = convertF.CelciusToK(celcius)
                    print(str(celcius) + " C = " + str(kelvin) + " K")
                    print()
                    print("Goodbye " + name)
                    exit()
                else:
                    if choice == 6:
                        yards = float(input("Value of yards to convert: "))
                        feet = convertF.yToFeet(yards)
                        print(str(yards) + " yards = " + str(feet) + " feet")
                        print()
                        print("Goodbye " + name)
                        exit()


            