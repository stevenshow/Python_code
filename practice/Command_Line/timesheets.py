def getInput():
    valid = False
    
    while not valid:
        time1 = input("Enter [first] time punch in Military time HHMM: ")
        time2 = input("Enter [second] time punch in Military time HHMM: ")
        
        if len(time1) > 4 or len(time2) > 4: 
            valid = False
            print("Please enter a valid 4 number time in HHMM format.")
        else:
            valid = True
    
    validateTime(time1, time2)
    
    return time1, time2

def validateTime(time1, time2):
    pass

def main():
    while True:
        time1, time2 = getInput()
        time1Hours, time1Mins = int(time1[0:2]), int(time1[2:4])
        time2Hours, time2Mins = int(time2[0:2]), int(time2[2:4])
        if time2Mins > time1Mins:
            finalHours = time2Hours - time1Hours
            finalMins = time2Mins - time1Mins
            print(str(finalHours) + ' Hours', str(finalMins) + ' Minutes')
        else: 
            finalHours = (time2Hours - 1) - time1Hours
            finalMins = -(time2Mins - time1Mins)
            print(str(finalHours) + ' Hours', str(finalMins) + ' Minutes')
main()



#TODO: 
# Handle if only 3 characters are entered 945 
# Handle if a non-int is entered 




# subtract the minutes from the minutes and the hours from the hours
# if the second times minutes are greater than the first, subtract 1 from the hours because that hour has not fully passed.
#   You would also negate this result due to it being negative 9:40am - 11:10am
# Possibly do all military time, or figure out how to gracefully handle AM -> PM time workings