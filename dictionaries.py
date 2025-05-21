#dictories we can store a branch of key value pairs

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

print(customer.get("birthdate"))
#it will show None object which represents the absent of the value

customer["age"] = 50
print(customer['age'])