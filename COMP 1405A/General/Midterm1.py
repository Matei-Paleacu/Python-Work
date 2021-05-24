def bigJumps(data: list, jump:float):
    jumpspots = list()
    for x in range(len(data)):
        if x == len(data) - 1:
            break
        use = data[x]
        use2 = data[x+1]
        usejump = float(use) + float(jump)
        usejump2 = float(use) - float(jump)
        print(use)
#        if data[x]< 0 :
#            use = use*-1
#        use2 = use + 1
        if float(use2) >= usejump or float(use2) <= usejump2:
            jumpspots.append(x)
            print(x)
            print(jumpspots)
    return jumpspots

data = [1,1,10,11,10,11,0,-1,-2.8]
jump = input("what jump would you like")
jumpspots = bigJumps(data,jump)
print(jumpspots)


