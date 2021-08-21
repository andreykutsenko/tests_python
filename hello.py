import random
import string

def generate_password(length: int) -> str:
    """Генерация пароля из цифр и букв"""
    items = string.ascii_letters + string.digits
    result = ''.join(random.choice(items) for i in range(length))
    print("Random string of length", length, "is:", result)

generate_password(10)