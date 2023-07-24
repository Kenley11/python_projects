import random
import string

length = int(input("Enter the desired length for the password: "))

def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate(length)
print("Generated password:", password)
