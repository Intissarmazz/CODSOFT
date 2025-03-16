import random
import string
print("_____Welcome to the Password Genertor made by Maaziz Intissar_____")
try:
    length = int(input("Enter the length of your password:"))
    if length < 1:
        print("The length of your passoword should be at least 1.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for x in range(length))
        print("Generated password :",password)
except ValueError:
    print("Enter a valid number!")









