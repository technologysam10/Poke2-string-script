import random
import keyboard
print("Welcome to poke2 script.")

#Get a random string

random_string = ''
 
for _ in range(10):
    # Considering only upper and lowercase letters
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    # Convert to lowercase if the flip bit is on
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    # Keep appending random characters using chr(x)
    random_string += (chr(random_integer))
 
print(random_string, len(random_string))

#type it

keyboard.write(random_string, delay=0.1)

