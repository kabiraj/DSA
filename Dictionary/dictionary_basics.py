
# 1) Declare dictionary
person = {
    "name": "Kabiraj Khatri",
    "profession": "Software engineer",
    "gender": "Male",
    "city": "Melbourne",
}
print("Initial:", person)
# Initial: {'name': 'Kabiraj Khatri', 'profession': 'Software engineer', 'gender': 'Male', 'city': 'Melbourne'}


# 2) Access values
print("Name:", person["name"])  # O(1) average
# Name: Kabiraj Khatri

# print(person["age"])  # KeyError if key does not exist
print("Age (safe get):", person.get("age"))  # O(1) average
# Age (safe get): None


# 3) Add / update values
person["hobby"] = ["Reading", "Playing games", "Hiking"]  # add key
person["city"] = "Sydney"  # update key
print("After add/update:", person)
# After add/update: {'name': 'Kabiraj Khatri', 'profession': 'Software engineer', 'gender': 'Male', 'city': 'Sydney', 'hobby': ['Reading', 'Playing games', 'Hiking']}


# 4) Delete values
# pop() removes by key and returns removed value
popped_hobby = person.pop("hobby")
print("Popped hobby:", popped_hobby)
# Popped hobby: ['Reading', 'Playing games', 'Hiking']

# popitem() removes and returns last inserted key-value pair
last_item = person.popitem()
print("Popitem removed:", last_item)
# Popitem removed: ('city', 'Sydney')

# del removes key directly (uncomment to test)
# del person["gender"]


# 5) Loop dictionary
print("\nLoop with items():")
for key, value in person.items():  # O(n)
    print(f"{key}: {value}")

print("\nLoop keys only:")
for key in person:  # same as person.keys()
    print(key, "->", person[key])


# 6) Useful built-ins
print("\nLength:", len(person))  # O(1)
print("Keys:", list(person.keys()))  # O(n)
print("Values:", list(person.values()))  # O(n)


# 7) Copy vs reference
ref_person = person  # same object reference
copy_person = person.copy()  # shallow copy

print("\nReference check:", ref_person is person)  # True
print("Copy check:", copy_person is person)  # False


# 8) Complexity quick notes
# Access / insert / update / delete: O(1) average
# Looping keys/items: O(n)
# Copy dictionary: O(n)

