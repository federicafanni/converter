def inchToCentimeter(inches): #Function inchToCentimetre that takes in inches and returns cms.
    valInCentimeters = inches * 2.54 #multiplies the argument by 2.54
    print(valInCentimeters, "cms") #and prints the result followed by cm.

def poundToKilogram(pounds):#Function poundToKilogram that takes in pounds and returns the amount in kilograms.
    kilograms = pounds * 0.45359237 #multiplies the argument by 0.45359237
    kgRounded = round(kilograms, 3) #3 rounds the result up to three decimals.
    print(str(kgRounded) + " kgs") #and prints the result followed by kg.

if __name__ == "__main__":
    inchToCentimeter(float(input("INCHES TO CMS CALCULATOR\nEnter the inches you want to convert into cms: ")))

    poundToKilogram(float(input("POUNDS TO KGS CALCULATOR\nEnter the amount in pounds to convert to kilograms: ")))    

    #The below is a conversion from stones to pounds using a lambda function.
    counterWeight = lambda stones: stones * 14 #multiplying the stone value by 14(because a stone is equal to 14 pounds)
    print(counterWeight(float(input("STONES TO POUNDS CALCULATOR\nEnter amount in stones to convert to pounds: "))), "pounds") 
