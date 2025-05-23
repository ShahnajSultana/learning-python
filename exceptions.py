#exception is a kind of error which crashes our program
try:
    age = int(input ('Age: '))
    income = 2000
    risk = income/age
    print(age)
    print(risk)

except ZeroDivisionError: #for handling age=0
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')