def cmToM(x:float):
    meters = x/100
    return meters

def pToLetter(x:float):
    if x == 0 or x < 50:
        letterGrade = "F"
        return letterGrade
    else:
        if x == 50 or x < 60:
            letterGrade = "D"
            return letterGrade
        else:
            if x == 60 or x < 70:
                letterGrade = "C"
                return letterGrade
            else:
                if x == 70 or x < 80:
                    letterGrade = "B"
                    return letterGrade
                else:
                    if x == 80 or x < 100:
                        letterGrade = "A"
                        return letterGrade

def LtoMl (x:float):
    milliliter = x*1000
    return milliliter

def gToKg (x:float):
    Kg = x/1000
    return Kg

def CelciusToK (x:float):
    kelvin = x + 273.15
    return kelvin

def yToFeet (x:float):
    feet = x * 3
    return feet

