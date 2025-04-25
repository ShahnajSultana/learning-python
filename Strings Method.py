course ='Python for Beginners'
print(len(course)) #general build method

print(course.upper())
print(course.lower())


print(course.find('o'))

print(course.find('O')) #it returns negative value because we don't have capital O

print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))

print('Python' in course) #expression which return boolean value
print('python' in course)

#find method returns the index but in operator produce the boolean value

print(course) #the string will not modify