import random

def generate_valid_email():
     return f"test_user_{random.randint(100000, 999999)}@mail.ru"

def generate_invalid_email():
     return f"test_user_{random.randint(100000, 999999)}mairu"

def generate_valid_password():
     return f"some_password_{random.randint(100000, 999999)}"