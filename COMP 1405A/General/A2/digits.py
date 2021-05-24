def passwordIsValid(passwd:str):
    passwordLenght = len(passwd)
    valid = False
    if passwordLenght >= 5:
        CheckDigits = digits(passwd)  
        if CheckDigits == True:
            CheckChar = specialChar(passwd)
            if CheckChar == True:
                CheckUpperCase = UpperCase(passwd)
                if CheckUpperCase == True:
                    CheckLowerCase = LowerCase(passwd) 
                    if CheckLowerCase == True:
                        CheckStart = PassStart(passwd)                          
                        if CheckStart == True:
                            valid = True
    return valid

def digits(enter:str):
    NUMBERS = "0123456789"
    digits = 0
    check = False
    for x in range(len(enter)):
        if enter[x] in NUMBERS:
            digits +=1
    if digits >= 2:
        check = True
    return check

def specialChar(passwd:str):
    specialCharacters = "!@#$%^_."
    check = False
    for x in range(len(passwd)):
        if passwd[x] in specialCharacters:
            check = True
    return check

def UpperCase(passwd:str):
    UpperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check = False
    for x in range(len(passwd)):
        if passwd[x] in UpperCaseLetters:
            check = True
    return check

def LowerCase(passwd:str):
    LowerCaseLetters = "acbdefghijklmnopqrstuvwxyz"
    check = False
    for x in range(len(passwd)):
        if passwd[x] in LowerCaseLetters:
            check = True
    return check

def PassStart(passwd:str):
    LowerCaseLetters = "acbdefghijklmnopqrstuvwxyz"
    firstChar = passwd[0].lower()
    check = False
    if firstChar in LowerCaseLetters or firstChar == "_":
        check = True
    return check

x = str(input("enter in a password"))
find  = passwordIsValid(x)
print(find)


    
