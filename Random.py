import random

random_number1 = input ("Enter start number ")
random_number2 = input ("Enter end number ")

randomest_number = random.randint(int(random_number1), int(random_number2))

print(f"The randomest number here is {randomest_number}")