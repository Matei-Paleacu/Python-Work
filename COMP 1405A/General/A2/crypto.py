def encrypt(message:str, shift:int, alphabet:str):
    y = 0                                                 # y is used as a counter for the character positions on the entered message
    encrypt = ""
    alphabetLength = len(alphabet)
    messageLength = len(message)
    x = 0                                                # x is used as a counter for the character position on the entered alphabet 
    while y < messageLength:                             # program repeats untile it reaches the end of entered string message
        if message[y] == alphabet[x].lower():
            newShift = x + shift
            if  newShift >= alphabetLength:              # checks to see if shift is greator or equal to alphabet legnth so it can wrap it around 
                newShift = newShift - alphabetLength
                encrypt = encrypt + alphabet[newShift]
                y += 1
                x = 0
            else:
                encrypt = encrypt + alphabet[newShift]
                y += 1
                x = 0
        else:
            x+=1
    return encrypt
    


# Password is Valid Solution:
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

def main():
    alphabet = input("please enter in alphabet you would like")
    shift = int(input("please enter in the shift"))
    message= input("please enter in the message to encrypt")
    alpha = encrypt(message, shift, alphabet)
    print(alpha)
    x = str(input("enter in a password"))
    find  = passwordIsValid(x)
    print(find)

if __name__ == "__main__":
    main()





















# All the code that is below is just some of my scrap/ extra code did not want to delete so I just commented it out
#alphabetList = alphabet[0:len(alphabet)]
 #   messageList = message[0:len(alphabet)]
  #  


 #   def encrypt(message:str, shift:int, alphabet:str):
 #   y = 0
 #   encrypt = ""
 #   i = len(alphabet)
 #   for x in range(len(message)):
 #       if message[y] == alphabet[x]:
 #           j = x + shift
 #           if  j >= i:
 #               j = j - i
 #               encrypt = encrypt + alphabet[j]
 #               y += 1
 #           else:
 #               encrypt = encrypt + alphabet[j]
 #               y += 1
 #               print(encrypt)
 #   return encrypt
    
#x = 0
#    i = 0
#    y = 0
#    while end == False
#        if i > 9: 
#        return end
#            if y == len(string):
#               y = 0 
#               x += 1
#               i += 1
#           else:
#               if x == string[y]
#                end = True
#               else:
#                   y +=1
#
