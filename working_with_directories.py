from pathlib import Path

path = Path("ecommerce")
print(path.exists())

#path = Path("emails")
#print(path.mkdir()) #create 'emails' directory
#print(path.rmdir()) #delete 'emails' directory

path = Path()
for file in path.glob('*.py'): #all the py file in the current directory
    print(file)