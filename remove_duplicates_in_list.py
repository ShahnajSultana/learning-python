numbers = [2,3,4,3,7,3,2,8]
uniques = [ ]

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)