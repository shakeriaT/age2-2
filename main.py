# this program calculates your age in year 2050
# input: none
# output: your current age followed by your age in 2050

# myCurrentAge = 25
# currentYear = 2024
# myNewAge = myCurrentAge + (2050 - currentYear)
myCurrentAge = "25"
currentYear = "2024"
myNewAge = int(myCurrentAge) + (2050 - int(currentYear))
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")