#basic calc

num1 = float(input("enter 1st num : "))
num2 = float(input("enter 2nd num : "))
operator = input ("enter +, -, * or / : ")

if operator == "+":
    print(f"both your numbers have been added i hope u r get better in ur maths :) here u go --> {num1+num2} have a nice day")
elif operator == "-":
    print(f"both your numbers have been subtracted i hope u r get better in ur maths :) here u go -->  {num1-num2} have a nice day")
elif operator == "*":
    print(f"i have successfully multiplied your numbers and the result isssssss............ --> {num1*num2} !!!!!!!!")
elif operator == "/":
    print(f"yeah division sucks anyone wud need calc for it ur division of 2 numbers is --> {num1/num2}")
else :
    print("is it too tuff to choose one of give operators? :) ")