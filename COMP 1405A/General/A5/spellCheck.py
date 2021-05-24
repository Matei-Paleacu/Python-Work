
def load_txt_file(fileName):
    ''' Reads a words from the text file 'filename' in the current directory. 
        Returns a list of lists of words that are spelt correctly.
            load_txt_file(filename:str) -> str[str[int]]
    '''
    words = [] 
    with open(fileName, "r") as f:
        for line in f:
            words.append( [str(val) for val in line.strip().strip(".").split(" ")] )
    return words


def save_txt_file(fileName,text):
    ''' This function uses for loops to iterate through the words and sentence of the desired text
        and writes it in the specified filename
    '''
    fileOut = open(fileName, "w")
    for sentence in text:                                                   #For loop goes through each sentence in the text
        for word in sentence:                                               #For loop goes through each word in the specified sentencce
            fileOut.write(listToString(word) + " ")
        fileOut.write(".")  
        fileOut.write("\n")                                                 #Add a newline char at the end of each sentence
    fileOut.close()
    return True


def save_word_txt_file(fileName,text):
    '''Function used when saving to a text file that has individual words instead of sentences'''
    fileOut = open(fileName, "w")
    for word in text:                                                       #For loops goes throught all the provided words
        fileOut.write(listToString(word) + "\n")                            #Adds a newline char to the end of each word
    return True


def save_mistakes_txt_files(fileName,text):
    '''Function is used to open and write to a txt file all the requested mistakes to store'''
    fileOut = open(fileName, "w")
    for ele in text:
        if str(ele).isnumeric() == True:                                    #If ele is a number then add a new line char to it when writing to the file
            fileOut.write(str(ele) + "\n")
        else:                                                               #Else add a comma to seperate elements in the text
            fileOut.write(str(ele) + ",")                                   
    return True



def listToString(s):
    ''' Converts a given list (s) to a string'''
    str1 = ""
    for ele in s:                                                           #For loops goes through each ele in the given list and adds it to a string to be returned 
        str1 += ele
    return str1

#def listToDict(s):
#    a_dict = {s[i]: s[i+1] for i in range(0, len(s) , 2)}
#    return a_dict

def spell(text, words, my_words):
    ''' Given the recently loaded text and list of correctly spelt words 
        it will read throught it to check for possible speeling errors
        using the correct words.txt file.
    '''
    possible_mistakes = []
    for sentence in text:
        for my_word in sentence:
            x = 0
            for correct_word in words:                                      #For loop to go throught the words txt file given with correctly spelt words
                if my_word.lower() == listToString(correct_word):
                    x += 1
            for my_correct_word in my_words:                                #For loop goes throught my correctly spelt words
                if my_word.lower() == listToString(my_correct_word):
                    x+=1
            if x == 0:  
                '''                                                         #If x is 0 this means that the word is not prested in the word txt file and not preseten in my text file
                This code is write for removing repeating mistakes
                if len(possible_mistakes) > 0:                               #If the list of mistakes is empty then append it to the list
                    y = 0
                    for mistake in possible_mistakes:                        #For loop checks if the found mistake has been found already befor
                        if my_word == mistake:
                            y +=1
                    if y == 0:                                                 #If y>0 this means that there are already values in the mistakes list however non of these values match the current value os it must be append to the list
                        possible_mistakes.append(my_word)
                else:
                    possible_mistakes.append(my_word)
                    '''
                possible_mistakes.append(my_word)
    return possible_mistakes

def mistakes (correction,error,mistakes_list):
    ''' Function takes the correction given by the user with the identified error along with the list of all potential errors
        and the list that contains the other identified and corrected mistakes.
        The function will reture the updated mistakes list if the error has not been repeated before.
    '''
    y = 1                                                               # y keeps track of the amoutn of times an error has been corrected and start at 1 as the minimu times an error can occur is 1 time
    x = 0                                                               #x represents the current position of ele in mistakes list that the program is going through
    for ele in mistakes_list:                                           #For loop to first check if the requested error has already been calculated
        if ele == error and mistakes_list[x+1] == correction:           #Finds a repeated requested error, if found returns the given list as the error has already been added yo the list
            y = mistakes_list[x+2] 
            y +=1
            mistakes_list[x+2] = y
            return mistakes_list
        x+=1

    mistakes_list.append(error)                                         #Adds each element seperate so I can acces each value as needed
    mistakes_list.append(correction)
    mistakes_list.append(y)
    return mistakes_list

def suggestions(mistakes,error,):
    ''' The suggestions functions takes in all the previous mistakes and the current error the program is goring through
        and provides a list of possible suggestions for the user to correct the error with. Furthermore
        the possible corrections are provided in decreasing order of the number of times that they have been used
        to corrct this word.
    '''
    relevent_error_list = []
    x = 0                                                               #x represents the current position of ele in mistakes list
    for ele in mistakes:                                                #for loop goes through each ele in the mistakes list
        if str(ele).isnumeric() == False:                               # if current ele is not a number 
            if ele.lower() == error.lower():                            #if comapres if the current error has been previously correct in the mistakes list(ele is an element in mistakes list)
                relevent_error_list.append(mistakes[x+2])               #if the error had been reapeted then both the correction is given from the mistakes list along with the number of times is hads been correctiong so it cna be sorted in suggestions based on relevence
                relevent_error_list.append(mistakes[x+1])
        x+=1
    if len(relevent_error_list) == 0:                                   #If the requested error has not been found in the mistakes list this means the program cannot give a suggestion foir a correction thus returning no suggestion
        return "[no suggestions]"
    number_of_times_repeated = 0                                                               # variable rep the number of times that an error has been corrected from the mistakes file
    for x in relevent_error_list[::2]:                                                         #once again in the for loop x goes to each number value stored in relevent_error_list
        if x > relevent_error_list[0]:                                                         #If a found x value is greator then the current x value at the list this means it has been repeated more times then whatever value is at the from of the list,
            y = relevent_error_list[number_of_times_repeated:number_of_times_repeated+2]        #Then the next two lines, first stores the (error,correction,number of times corrected) which arr then append to the start of the list and removed from there location in the list
            del relevent_error_list[number_of_times_repeated:number_of_times_repeated+2]
            z = 0
            for ele in y:                                                                      #This for loop quickly goes through the stores y values which is (error,correction,number of times corrected) and adds each ele to the list so it is just a part of the list and does not creat an additional list inside of the list
                relevent_error_list.insert(z,ele)
                z+=1                                                                            #Variable z just keeps track of which position of element we are at in our list as we just want to append the stored mistake at the start of our list
        x = relevent_error_list[number_of_times_repeated]
        if x == relevent_error_list[0]:                                                         #If the current x value (which represents one of the number of times a error has been repeated) is the same as the fron value then add this error after of the first initial value, the rest of the code as previously explained above
            y = relevent_error_list[number_of_times_repeated:number_of_times_repeated+2]
            del relevent_error_list[number_of_times_repeated:number_of_times_repeated+2]
            z = 2                                                                                #Setting z as 2 allows the for loop that follows that goes through and adds the requested error to run and add it after the first error in the relevent error list
            for ele in y:
                relevent_error_list.insert(z,ele)
                z+=1
        number_of_times_repeated+=2                                                             #adds 2 each time as the numbers in the mistake file occur every 2 elements
    for ele in relevent_error_list:                                                             #For loop goes through  each element and if the element is a number then remove it from the lsit(this is jsut so it looks as requested, only a list of relevent word suggestions for correction)                           
        if str(x).isnumeric() == True:
            relevent_error_list.remove(ele)
    return relevent_error_list



# Your "program" is driven by the main method
def main():
    words = load_txt_file("words.txt")
    my_words = load_txt_file("mywords.txt")
    mistakes_list = []
    word_suggestion = []
    user_input =""
    while user_input != "quit":                                        #While loop will break if the user enters quit, it will then uipdate a write to the mistaktes txt file and the mywords txt file
        try:                                                           #Main code is wrapped in a try and exept, if any errors come up a "not a valid input" message will apear on the screen and then the program will ask for a command again
            user_input = input("Enter command")
            if user_input[:4] == "load":                               #If the first 4 char are load then it give the char after as the filename to the load file function
                text = []
                text = load_txt_file(user_input[5:])
            if user_input == "spell":                                   #If user types in spell then both my wrds and the words txt file are given to the spell function along with the mytext file
                potential_mistake = spell(text,words,my_words)
                if len(potential_mistake) > 0 :
                    for error in potential_mistake:
                        word_suggestion = suggestions(mistakes_list,error)
                        print("Potential mistake:" , error ,word_suggestion)
                        user_input = input("Action:")
                        if user_input == "":
                            my_words.append(error)
                        if user_input =="quit":                             #Add an additional quit just in case the user quits mid procces to correcting there text
                            break
                        else:                                               #Else is for if the user types in a correction they would like to make
                            mistakes_list = mistakes(user_input,error,mistakes_list)
                            current_sentence = 0                                           # varaible current_sentence keeps track of the sentence we are currently looking through
                            error_has_been_found = 0                                           #variable error_has_been_found is used to identify if a error has already been replaced then will break out of the for loops 
                            for sentence in text:
                                word_position = 0                                       # varaible word_position keeps track of what position we are in the senetce specifically used for what word
                                for words in sentence:
                                    if words.lower() == error.lower():              #Goes throught the test and finds the identified error and once found replaced it with the requested value
                                        text[current_sentence][word_position] = user_input
                                        error_has_been_found +=1
                                        break
                                    word_position+=1
                                current_sentence+=1
                                if error_has_been_found > 0:
                                    break
            if user_input[:4] == "save":                                    #if the user specifies to save a specifice file the program will go and save it using the save_txt_file
                saved_text = save_txt_file(user_input[5:],text)
        except:
            print("not a valid input")
    saved_text = save_word_txt_file("mywords.txt",my_words)
    saved_mistakes = save_mistakes_txt_files("mistakes.txt",mistakes_list)





# Guard for main function 
if __name__ == "__main__":
    main()