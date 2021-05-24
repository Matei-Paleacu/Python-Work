month = str(input("Which month?"))
days = None
jan = "january" 
feb = "febuary"
mar = "march"
apr = "april"
may = "may"
jun = "june"
jul = "july"
aug = "august"
sept = "september"
octo = "october"
nov = "november"
dec = "december"

if month == jan or month == mar or month == may or month == jul or month == aug or month == octo or month == dec:
    print(month + " has 31 days")
    exit()
if month == apr or month == jun or month == sept or month == nov:
    print(month + " has 30 days")
    exit()
if month == feb:
    leapYear = int(input("Which year?"))
    divisible_4 = leapYear%4
    divisible_100 = leapYear%100
    divisible_400 = leapYear%400
    if divisible_4 > 0:
        print(month + " has 28 days in " + str(leapYear))
        exit()
    if divisible_4 == 0 and divisible_100 == 0 and divisible_400 > 0:
        print(month + " has 28 days in " + str(leapYear))
        exit()
    else:
        print(month + " has 29 days in " + str(leapYear))
else: 
    print (month + " is noth a valid month")