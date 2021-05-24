d1 = dict()
print("empty dictionary d1" , d1)

d2 = {}
print("empty dictionary d2" ,d2)
print(type(d2))

d = {"one":1,"two":2,3:3} #acces dictionary by keys that are stored
print(d)
print(d['two'])
print(d[3])

if 4 in d:
    print(d[4])
else:
    print("4 is not in the dictionary as a key")

print("# of key :value paris is", len(d))
d["four"] = 4 #adds four:4 to dictionary
print(d)
d["two"] = 69 #if two already exist overide the existing sotred value at key two if not add it to dictionary
print(d)

mapping = {1:'1st',2:'2nd',3:"3rd", 4:"4th"} # keys have to be unique
print(mapping)

popped = mapping.pop(4)   #pop removes something from a dictionary and retures the value
print(popped, "was removed")
print(mapping)

for key in mapping:                 #prints out the key and the key value 
    print(key, mapping.get(key))