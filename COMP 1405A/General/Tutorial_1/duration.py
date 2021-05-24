
#weeks = days/7
#months = days/30
#years = days//365
#print(str(days) + " days is equivilant to " + str(weeks) + " weeks")
#print(str(days) + " days is equivilant to " + str(months) + " months")
#print(str(days) + " days is equivilant to " + str(years) + " years")

days = int(input("How many days?"))
years = days//365
years2 = years*365
daysLeft = days - years2
months = daysLeft//30
months2 = months*30
daysLeft = daysLeft - months2
weeks = daysLeft//7
weeks2 = weeks*7
daysLeft = daysLeft - weeks2

print(str(days) + " days is " + str(years) + " year, " + str(months) + " months, " + str(weeks) + " weeks, and " + str(daysLeft) + " days.")









