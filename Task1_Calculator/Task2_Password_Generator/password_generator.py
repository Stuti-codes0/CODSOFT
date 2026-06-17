import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&!"
length = int(input("How many characters do you want in your password? "))
characters = letters + numbers + symbols
password = ""
for i in range(length):
    password += random.choice(characters)

print("\nYour Password is:", password)
print("Keep it safe!")
