time = float(input("Enter the number of hours studied :"))

if time <= 0.0:
    print ("time doesnt go in negative (-_-) enter the hours studied correctly !!!")
elif time >= 4.0:
    print ("the day was productive")
elif time >=1.0 and time <4.0:
    print ("the day wasnt much productive")
else: 
    reason = input("give the reason for wasting the day : ")
    print (f"'{reason}' like really?? you call this a reason ?? no reason is worth wasting entire day !!!! lock in !!! ")