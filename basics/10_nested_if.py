age = int(input("Enter your age:"))
has_id = input("Do you have an ID? (yes/no):")
if age >= 18:
    if has_id == "yes":
        print("You can enter")
    else:
        print("You need an ID")
else:
    print("You are an under 18")


marks = int(input("Enter your marks:"))


if marks >= 35:
    if marks >= 80:

        print("Excellent")
    else:
        print("you passed")
else:
    print("you failed")


username = input("Enter your username:")
password = input("Enter password:")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("user not found")


