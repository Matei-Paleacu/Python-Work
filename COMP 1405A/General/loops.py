number = 1
multipleFound = False
while number <= 100 and not multipleFound: # Called a flag used to end a loop instead of using (break) to break out of it
    if number % 3 == 0 and number % 7 == 0:
        print(number)
        multipleFound = True  # Once the number that meets the requirments is found then we set the bool to true to end the loop as it no longers meets the requirment at the start of the loop
    number += 1 

word = "theWord is this"

index = 0                               
while index < len(word):            #uses the index to print out every letter of the given string
    print(word[index])
    index += 1 

inWord = "xEAmPLe"
outWord = ""

for c in inWord:               # for loop that goes through the given string and using the (upper) funvtion to identify ig the char is a upper case or a lower case
    if c.isupper():
        outWord += c
        print(c, "upper case")
    else:
        print(c, "lower case")

print("all capse", outWord)


nums = [1,2,3,5,8]
print("befor", nums)
for index in range(len(nums)): # range is used for the for loop to know for it go until it reaches the end of the list
    nums[index] *= 2

print("after", nums)

print(list(range(0,12,3))) # creates a liost that goes from 0-12 but no including 12 and prints out every third number so 0,3,6,9

nums2 = [1,4,5,7,8]
print( 4 in nums2)  # checks to see if the requested value is in the givien list
print( 9 in nums2)

#def myIn (sequence,target):         # this function is that the (in) function does from the privious line.
#    index = 0
#    while index <len(sequence):
#        if target == sequence[index]:
#            return True
#        index += 1
#    return False