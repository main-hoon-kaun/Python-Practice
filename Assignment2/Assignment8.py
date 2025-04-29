password=input("Enter your password: ")
if len(password) < 6:
    print("Password Strength: Too short")
elif len(password) <= 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
