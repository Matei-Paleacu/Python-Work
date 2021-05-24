def findbyDomain2(domain:str, data:list()):   # Has 2 nested for loops the first ones switched between the cat , dog , eel etc lits, and the second one goes throught the resective lists to fine the entered domain
    dataString = data[0]
    dataList1 = dataString.split("_")
    things = ""
    name = ""
    numberofDomains = 0
    output = list()
    for x in range(len(dataList1)):
        things = dataList1[x]
        thingsList = things.split(",")
        name = thingsList[0]
        for x in range(len(thingsList)):
            if domain in thingsList[x]:
                numberofDomains += 1
        if numberofDomains < 1 :
            output.insert(x," ")
        else:
            outputString = name + ":" + str(numberofDomains) + ","
            numberofDomains = 0
            output.insert(x,outputString) 
    return output


def emailsByAge(lower:int, upper:int, data:list()): # Similar to the code above I broke the larger string into smaller individual strings then lists for each thing (cat,dog,eel)
    dataString = data[0]
    dataList = dataString.split("_")
    avgEmail = 0
    output = list()
    foundAge = list()
    foundValue = list()
    lengthofOutput = (int(upper) - int(lower) + 2)
    for x in range(len(dataList)):
        things =dataList[x]
        thingsList = things.split(",")
        for x in range(lengthofOutput):
            ageI = thingsList[1]
            age = int(lower) + int(x) 
            if str(age) == ageI:                
                for x in range(len(things)):    # Found out how many "@" symbols there are in the iddividual things array 
                    if things[x] == "@":
                        avgEmail+=1
                foundAge.append(age)                # make an list correspoding the all the ages of each thing 
                foundValue.append(float(avgEmail))  # and the corrispoding number of "@" symbols in the list
                avgEmail = 0
                break

    for x in range(lengthofOutput-1):   #Creats an empty list then lenght of the required output and then populates it based on the specific values found
        output.insert(x,0) 
    output.insert(0,int(lower))
    for x in range(len(foundAge)):
        output[foundAge[x] - int(lower) + 1] = foundValue[x]
    return output

def main():
    data = ["cat,12,nothing to see here,cat@yahoo.ca,kit@carleton.ca,c@yahoo.ca_dog,7,top.dog@hotmail.com_eel,10,empty,eel@yahoo.ca,eel@hotmail.com,eel@eel.com_pig,16,top.pig@carleton.com"] #The individial list of cat dog and eel are all seperated by an "_" to help me distigues between them, more list cxan be added aslong as ther is an "_" to seperate them
    domain = input("Please enter in the domain you are looking for")
    found = findbyDomain2(domain, data)
    print(found)
    lower = input("Please enter in a lower value")
    upper = input("Please enter in a upper value")
    found2 = emailsByAge(lower,upper,data)
    print(found2)

if __name__ == "__main__":
    main()


#Extra code:
#def findbyDomain(domain:str, data:list()):
#    dataString = data[0]
#    numberofEmails = 0
#    dataList = dataString.split(",")
#    name = dataList[0]
#    for x in range(len(dataList)):
#        if domain in dataList[x]:
#            numberofEmails+=1
#    output = [name + ":" + str(numberofEmails)]
#    if numberofEmails < 1:
#        output = []
#    return output



    
