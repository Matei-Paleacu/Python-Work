# dictionary1 = dict()
dictionary1 = {"one":1,"two":2,"three":3,"four":4}
print(dictionary1)
print(len(dictionary1))
print(dictionary1["two"])
print(dictionary1["three"])

nums = {0:"0th",1:"1st", 2:"2nd", 3:"3rd"}
print(nums)
print(len(nums))
print(nums[1])
nums[0] = 3                 #How to change a value in a dictionary
nums[4] = 4                 #If the asked value is not found then add it to the dictionary
print(nums)

keys = nums.keys()          # Returns all the keys values in a dictionary
print(keys)
values = nums.values()      # Returns all the values in the dictionary
print(values)

d = {"one":1,"two":2,"cat":3}
print(d)
d.pop("cat")
print(d)
val = d.pop("two")
print(d)

d2 = {"apple":1,"banana":2,"orange":3}
print(1 in d2) # the in function loks for the key value nerver the actaully value
print(d2.pop("apple","key not found")) #looks to remove a specified key, if not it returns key not found
print(d2)

d3 = {"key1":1,"key2":2,"key3":3}
print(d3.get("key1","not here")) #get retrives a value of a key without removing the pair

for key in d3:
    print("key:", key ,"value:",d3[key])

def merge1(d1,d2):
    finalD = d1
    print(finalD)
    for key in d2:
        finalD.update({key:d2[key]})
    return finalD

def merge2(d1,d2):
    finalD = d1
    for key in d1:
        if key in d2.keys():
            finalD.update({key:[d1[key],d2[key]]})
        else:
            finalD.update({key:d1[key]})
    for key in d2:
        if key not in finalD:
            finalD.update({key:d2[key]})
    return finalD

def top3(d:dict):
    keys = list()
    for key in d:
        keys.append(key)

    top3 = [[d[keys[0]],keys[0]] , [d[keys[1]] ,keys[1]] , [d[keys[2]] ,keys[2]]]
    for key in d:
        if d.get(key) > top3[2][0]:
            top3[2] = [d.get(key), key]
        if d.get(key) > top3[1][0]:
            top3[2] = top3[1]
            top3[1] = [d.get(key), key]
        if d.get(key) > top3[0][0]:
            top3[1] = top3[0]
            top3[0] = [d.get(key), key]
    
    return top3


d5 = {"a":100,"b":200,"c":300}
d6 = {"a":300, "b":200,"d":400}
print(merge1(d,d2))
print(merge2(d5,d6))

s = set()
s.add(10)
print(s)
print(len(s))
s.add(5)
print(len(s))

d7 = {"a":100,"b":200,"c":300, "d":500, "e":600}
print(top3(d7))

print(d7.keys())
print(f"i have ",6, "appelse")
