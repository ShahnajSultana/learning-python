import random

for i in range(3):
    print(random.random())

print("\n")

for i in range(3):
    print(random.randint(10,20))


print("\n")

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)