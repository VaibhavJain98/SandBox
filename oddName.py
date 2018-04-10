"""Vaibhav"""

name = (input("Enter a name :"))
while name == "" :
    print("Invalid Value")
    name = input("Enter a name :")

print(name[::2])