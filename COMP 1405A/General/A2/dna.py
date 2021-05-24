def pair(strand1:str):
    strand2 = ""
    for x in range(len(strand1)):
        if strand1[x] == "A" or strand1[x] == "a":
            strand2 = strand2 + "T"
        if strand1[x] == "T" or strand1[x] == "t":
            strand2 = strand2 + "A"
        if strand1[x] == "C" or strand1[x] == "c":
            strand2 = strand2 + "G"
        if strand1[x] == "G" or strand1[x] == "g":
            strand2 = strand2 + "C"
    return strand2

def compress(strand:str):
    y = 0                                      #Counter used to keep track of how many times each letter has apeared 
    numbers = ""
    letters = ""
    compressed = ""
    z = len(strand)
    z = z-1
    for x in range(len(strand)):
        if x == z:
            numbers = numbers  + str(y+1)
            letters = letters + strand[x]  
            break
        if strand[x] == strand[x+1]:
            y+=1
        else:
            numbers = numbers  + str(y+1) 
            letters = letters + strand[x] 
            y = 0
    for x in range(len(numbers)):
        compressed = compressed + numbers[x] + letters[x]
    compressed = compressed.replace('1',"")
    return compressed

def expand(compressedStrand:str):
    expanded = ""
    findNumbers = True
    number = ""
    letter = ""
    previousLetter = ""
    for x in range(len(compressedStrand)):
        if compressedStrand[x].isnumeric() == True:
            number = number + compressedStrand[x]
            while findNumbers == True:                                  # While loop that is always true until I break out of it
                if compressedStrand[x+1].isnumeric() == True:
                    number = number + compressedStrand[x+1]
                    x+=1
                else:
                    letter = compressedStrand[x+1]
                    if previousLetter != letter:
                        expanded = expanded + (letter* int(number))
                    break
            previousLetter = letter                                         #This is used to make sure if there is a nuber like 12 befor G I dont want it to add first 12 G then 2 G so i check if the letter has already been used the previous turn
            letter = ""
            number = ""
        else:
            if x == 0:
               expanded = expanded + compressedStrand[x]
            else: 
               if compressedStrand[x-1].isnumeric() == False:
                    expanded = expanded + compressedStrand[x]           
    return expanded



#AAATTGCCC
#3AT12GA
def main():
    firstSequence = input("Please enter in the first sequence of DNA you are interested in")
    secondSequence = pair(firstSequence)
    print(secondSequence)
    notCompressed = input("Please enter in the first sequence of DNA you are interested in compressing")
    compressed = compress(notCompressed)
    print(compressed)
    compressed2 = input("Please enter in a DNA sequence you would like to expand")
    expanded = expand(compressed2)
    print(expanded)

if __name__ == "__main__":
    main()

#This is just some extra code I wanted to keep:
#def compress(strand:str):
#    y = 0
#    positionList = list()
#    strandList = list(strand)
#    period = "."
#    z = len(strand)
#    z = z - 1
#    for x in range (len(strand)):
#        if x == z:
#            break
#        if strand[x] != strand[x+1]:
#            positionList.insert(y,x)
#            y+=1
#            print(strandList)
#            print(positionList)
#    for x in range(len(positionList)):       
#        strandList.insert(positionList[x]+1,period)
#    print(strandList)  
#    return True

