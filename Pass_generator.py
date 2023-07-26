import re
import random
import string

def password_gen():
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W])[A-Za-z0-9\W]{8,}$", password):
            return password

password = password_gen()
print("Generated password:", password)
