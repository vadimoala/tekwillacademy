# Create a Dictionary:
# English: Create a dictionary named my_dict with three key-value pairs, where keys are fruits and values are their respective colors.
# Romanian: Creați un dicționar numit my_dict cu trei perechi cheie-valoare, unde cheile sunt fructe și valorile sunt culorile lor.

my_dict = {
    "kiwi": "green",
    "cherry": "rose",
    "lemon": "orange"
}


# Accessing Values:
# English: Print the color of the fruit "apple" from my_dict.
# Romanian: Afișați culoarea fructului "măr" din my_dict.

print(my_dict["kiwi"])


# Adding Elements:
# English: Add a new key-value pair to my_dict, where the key is "banana" and the value is its color.
# Romanian: Adăugați o nouă pereche cheie-valoare în my_dict, unde cheia este "banana" și valoarea este culoarea acesteia.

my_dict["apple"] = "red"
print(my_dict)


# Updating Values:
# English: Change the color of the fruit "apple" to "green" in my_dict.
# Romanian: Schimbați culoarea fructului "măr" în "verde" în my_dict.

my_dict["lemon"] = "yellow"

# Deleting Elements:
# English: Remove the key-value pair for the fruit "banana" from my_dict.
# Romanian: Ștergeți perechea cheie-valoare pentru fructul "banana" din my_dict.

my_dict.pop("cherry")


# Looping Through Keys:
# English: Print all the keys in my_dict using a loop.
# Romanian: Afișați toate cheile din my_dict folosind o buclă.

for key in my_dict:
    print(key)


# Looping Through Values:
# English: Print all the values in my_dict using a loop.
# Romanian: Afișați toate valorile din my_dict folosind o buclă.

for values in my_dict.values():
    print(values)


# Looping Through Key-Value Pairs:
# English: Print all key-value pairs in my_dict using a loop.
# Romanian: Afișați toate perechile cheie-valoare din my_dict folosind o buclă.

for key, values in my_dict.items():
    print(key, values)


# Merging Dictionaries:
# English: Create a new dictionary named additional_dict with two key-value pairs and merge it with my_dict.
# Romanian: Creați un dicționar nou numit additional_dict cu două perechi cheie-valoare și îmbinați-l cu my_dict.

additional_dict = {
    "pear": "rose",
    "apricot": "pink"
}
my_dict.update(additional_dict)


# Checking if a Key Exists:
# English: Check if the key "orange" exists in my_dict and print the result.
# Romanian: Verificați dacă cheia "orange" există în my_dict și imprimați rezultatul.

if "banana" in my_dict:
    print("key exists")
else:
    print("key does not exists")


# Getting a Default Value:
# English: Access the value for the key "grape" from my_dict, if it doesn't exist, print "Not found".
# Romanian: Accesați valoarea pentru cheia "grape" din my_dict, dacă nu există, imprimați "Nu s-a găsit".

print(my_dict.get("grape", "no exists"))
print(my_dict.get("lemon", "no exists"))


# Nested Dictionaries:
# English: Create a dictionary nested_dict where each key is a person's name, and the value is another dictionary containing their age and gender.
# Romanian: Creați un dicționar nested_dict în care fiecare cheie este numele unei persoane, iar valoarea este un alt dicționar care conține vârsta și genul lor.

nested_dict = {
    "Vadim": {"age": 32, "gender": "male"},
    "Ana": {"age": 27, "gender": "female"}
}


# Accessing Nested Values:
# English: Print the age of the person named "John" from nested_dict.
# Romanian: Afișați vârsta persoanei cu numele "John" din nested_dict.

print(nested_dict["Vadim"]["age"])


# Updating Nested Values:
# English: Update the age of the person named "John" in nested_dict to 30.
# Romanian: Actualizați vârsta persoanei cu numele "John" în nested_dict la 30.

nested_dict["Vadim"]["age"] = 30


# Looping Through Nested Dictionaries:
# English: Print all the names and ages from nested_dict using a loop.
# Romanian: Afișați toate numele și vârstele din nested_dict folosind o buclă.

for names, ages in nested_dict.items():
    print(names, ages["age"])