# Random Head and Tails program exercise

import random

coin = random.randint(1,2)
if coin == 1:
    print("Heads")
else:
    print("Tails")

# Random Who Will Pay the Bill program exercise

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

bill = random.randint(0,4)
print(friends[bill])

# OR

print(random.choice(friends))