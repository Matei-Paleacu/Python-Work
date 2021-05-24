import math
#for i in range(13):
#    print(f"{i:03}", i**3,math.sin(i))


#for i in range(0,500,50):   #0 - 500 but adds 50 so it goes 0,50,100
 #   print(f"{i:03}", f"{i**3:12}", f"{math.sin(i):+12.3f}")


#for i in range(0,500,50):   
 #   print(f"{i:4}", f"{i:4x}", f"{i:o}", f"{i:e}")

#for i in range(0,35):   
#    print(f"{i:4}", f"{i:4x}", f"{i:o}", f"{i:e}") # Prints variable i in base 8, scientific notation and also with 4 spaces

import datetime
d = datetime.date(2020,10,8)
print(d) # Prints out the year the month and the day
d2 = f"{d} finer details {d:%A, %B, %d, %Y}" # Prints out the exact day of the week as A, month as B, day # d, and year as Y
print(d2)

empty = list() # makes an empty list

myList = [1,2,3,'cat',False,8]
print(myList[0:6:2]) # 0 is the start, 6 is the stop, and 2 is the skip pattern 
myList.append("Matei") # modifies and adds something to me list
print(myList) # prints out a specific value of my list
a =[1,2]
b = [3,4,5]
a.extend(b) # adds second list "b" to first list "a"
print(a)
a.insert(2,69) #insert a specified value at a specific place
print(a)
c = [3,7,54,9,1,4]
c.sort()
print(c) # sorts list from smallest to greatest 