weight = float(input("Enter your weight :"))
unit = input("unit is in Kilogram or pounds (K or L):")

if unit == "K" :
    print(f"Your weight in pounds is {weight*2.205} pounds")
elif unit == "L" :
    print(f"Your weight in Kilogram is {weight/2.205} Kilos")
else :
    
    print("invalid input")