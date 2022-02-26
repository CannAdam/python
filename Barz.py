import random

bars = ["mad hatter", "twistys", "hideaway"]

people = ["scott", "maile", "chuck"]

random_bar = random.choice(bars)
random_people = random.choice(people)

print(f"How would you like to go to {random_bar} with {random_people}?")