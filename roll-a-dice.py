import random

while (response == "y" & response == "n"):
    yes = 6
    no = random.randint(1,6)

if response == "y":
    print(yes)

elif response == "n":
    print(no)