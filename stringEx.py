#username exercise
# 1. username is no more then 12 char
# 2. username must no contain spaces 
# 3. username must not contain digits 

username = input("enter your username :")

if len(username) > 12 :
    print("username cannot exceed 12 characters")

elif not username.find(" ") == -1 :
    print("username cannot contain spaces")

elif not username.isalpha():
    print("username cannot contain digits")

else :
    print (f"welcome {username}")