import time
import random
import keyboard

print("Welcome to poke2 script.")



#Get a random string



printit = input("Should It print each string along with typeing it (True/False)")

isOn = True

        

while isOn:
    random_string = ''
    for _ in range(30):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    keyboard.write(random_string, delay=0.15)
    keyboard.press_and_release("enter")