import math
def areacircle(radius:int):
    pi = math.pi
    radius2 = int(radius) *int(radius)
    area = float(pi) * float(radius2)
    return area

true = True
while true == True:
    x = input("what radius would you like:")
    if x.lower() == "quit":
        print("end of the program")
        break
    else:
        area = areacircle(x)
        print(area)
    
def RightAlight(number:int, size:int, zero=bool):
    number_as_string = str(number)
    if len(number_as_string) > size:
        return number
    else:
        filler = ""
        if zero == True:
            filler ="0"
        else:
            filler = ""
    return filler*(size - len(number_as_string)) + number_as_string


print(RightAlight(12,5,True))


