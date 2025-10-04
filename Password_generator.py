import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Your secure password is:", generate_password(length))
