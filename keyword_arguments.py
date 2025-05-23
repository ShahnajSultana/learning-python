#prefix the argument of the parameter
'''
Use positional arguments for most cases.
If a function takes multiple numerical values and it's unclear what each one represents, use keyword arguments for clarity.

And if you are passing both potional and keyword argument, the use the keyword argument after the positional argument
'''
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abroad')


print("Start")
#greet_user(first_name="John","Smith") #shows error
greet_user("John",last_name="Smith")
print("Finish")