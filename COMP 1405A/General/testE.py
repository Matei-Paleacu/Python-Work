e = [1,2,3]
e = [4,5,6] + e
print(e[:5])
for i in range(9,3,-2):
    print(i)
#    print(e[i])
print(e)
e.insert(3,9)
print(e)

x = [1,2,4,1]
x.remove(1)
print(x)
x.pop(2)
print(x)

dicts ={1:"amtei",2:"lucas",3:"panda"}
dicts[3] = 1
print(dicts)
print(dicts.get(5,"kk"))
s1 = "matei"
print(s1[2])
#x = input("matei")
#y = input("matei")
#x = x + y
print(x)
print(str([1,2,3,4].append([5,6,7])))
print(str([1,2,3,4,5,6]))
print(f"I have {44} poitat with {96} monkeys ")