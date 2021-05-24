#acc = 0
#count = 0
#bound = 100
#while count < bound:
#    count+=1
#    acc+=1
#print(acc)

import math
import random

print(math.sqrt(2.0)) #square roots 2
print(math.sin(60)) # does sin of andle 60 degrees
print(math.pi) # prints how the value for pi
print(math.e) # porints out the value for e 
diceroll = random.randrange(1,7)
prob = random.random()
print(diceroll) # produced a random value given a range [1 - 7)
print(prob)   # produced a randome value between [0.0 - 0.1) floating point





# Names and Ages
def hastages(age:int):
    hastage = ""
    for x in range(age):
        hastage += "#"
    return hastage
print("name : Matei Paleacu")
print("id:1000111")
print("age: 17")
mage = 17
outputH = hastages(17)
print(outputH)
name = input("enter your name:")
sID = input("enter your id:")
age = input("enter your age:")
print("name:" + name)
print("id:" + sID)
print("age:" + age)
outputIH = hastages(int(age))
print(outputIH)
if mage > int(age) :
    print("Matei Paleacu is older than " + name)
if int(age) > mage:
    print(name + "Is older than Matei Paleacu")
if int(age) == mage:
    print("Matei Paleacu and "+ name +" are the same age")

def more(char1:str, char2:str, word:str):
    char1app = 0
    char2app = 0
    for x in range(len(word)):
        if char1[0] == word[x]:
            char1app+=1
        if char2[0] == word[x]:
            char2app+=1
    if char1app > char2app:
        return char1
    elif char2app > char1app:
        return char2
    elif char1app == 0 and char2app == 0:
        nothing =""
        return nothing
    elif char1app == char2app:
        same = char1+char2
        return same
    
print("there is more", more('a','b',"cattab"))
print( 'there is more', more('A', 'a', 'dog'))
print( 'there is more', more('a', 'b', 'bagab'))
    
