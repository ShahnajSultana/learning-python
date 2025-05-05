numbers=[5, 2, 1, 7, 4, 5]
numbers2 = numbers.copy() #copy of the number list.here no impact will appear for adding or removing

numbers.append(20)
numbers.insert(0,10)
numbers.remove(1)
numbers.pop() #last item of the list
#numbers.clear() #clear all the items of the numbers list
print(numbers)
print(numbers.index(5)) #the index of the item
print(50 in numbers) #check 50 in available or not in the list
print(numbers.count(5)) #how many 5 is available of the list

numbers.sort() #sort ascending order
print(numbers)

numbers.reverse() #sort descending order
print(numbers)

print(numbers2)