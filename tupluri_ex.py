# Sure, here are the exercises with both English and Romanian versions along with their basic Python solutions:

# ### Tuple Exercises (Exerciții cu tuple):

# 1. **Creating Tuples (Crearea de tuple):**
#    English: Create a tuple named `my_tuple` containing three elements: "apple", "banana", "orange".
#    Romanian: Creați o tuplă numită `my_tuple` care conține trei elemente: "apple", "banana", "orange".

my_tuple = ("apple", "banana", "orange")


# 2. **Accessing Elements (Accesarea Elementelor):**
#    English: Print the second element of `my_tuple`.
#    Romanian: Tipăriți al doilea element al lui `my_tuple`.

print(my_tuple[1])


# 3. **Immutable Nature (Natura imutabilă):**
#    English: Try to change the first element of `my_tuple` to "pear" and observe the error.
#    Romanian: Încercați să schimbați primul element al lui `my_tuple` în "pear" și observați eroarea.

#my_tuple[0] = "pear"


# 4. **Concatenating Tuples (Concatenarea Tuplurilor):**
#    English: Create a new tuple named `other_tuple` with two elements: "grape" and "kiwi", then concatenate it with `my_tuple`.
#    Romanian: Creați o tuplă nouă numită `other_tuple` cu două elemente: "grape" și "kiwi", apoi concatenați-o cu `my_tuple`.

other_tuple = ("grape", "kiwi")
combined_tuple = my_tuple + other_tuple
print(combined_tuple)


# 5. **Slicing Tuples (Decuparea Tuplurilor):**
#    English: Print the elements from index 1 to 2 (inclusive) from `my_tuple`.
#    Romanian: Tipăriți elementele de la indexul 1 la 2 (inclusiv) din `my_tuple`.

print(my_tuple[1:3])


# 6. **Tuple Length (Lungimea Tuplului):**
#    English: Print the length of `my_tuple`.
#    Romanian: Tipăriți lungimea lui `my_tuple`.

print(len(my_tuple))


# 7. **Looping Through Tuples (Parcurgerea Tuplurilor):**
#    English: Use a loop to print all elements of `my_tuple` on separate lines.
#    Romanian: Utilizați un ciclu pentru a tipări toate elementele lui `my_tuple` pe linii separate.

for element in my_tuple:
    print(element)


# 8. **Tuple Unpacking (Despachetarea Tuplurilor):**
#    English: Unpack `my_tuple` into three variables: `fruit1`, `fruit2`, and `fruit3`, then print them.
#    Romanian: Despachetați `my_tuple` în trei variabile: `fruit1`, `fruit2` și `fruit3`, apoi tipăriți-le.

fruit1, fruit2, fruit3 = my_tuple
print(fruit1, fruit2, fruit3)


# 9. **Checking Membership (Verificarea Apartenenței):**
#    English: Check if "apple" is present in `my_tuple` and print the result.
#    Romanian: Verificați dacă "apple" este prezent în `my_tuple` și tipăriți rezultatul.

print("apple" in my_tuple)


# 10. **Counting Occurrences (Numărarea Aparițiilor):**
#     English: Count the number of times "apple" appears in `my_tuple` and print it.
#     Romanian: Numărați de câte ori apare "apple" în `my_tuple` și tipăriți rezultatul.

print(my_tuple.count("apple"))


# 11. **Finding Index (Găsirea Indexului):**
#     English: Find the index of "orange" in `my_tuple` and print it.
#     Romanian: Găsiți indexul lui "orange" în `my_tuple` și tipăriți-l.

print(my_tuple.index("orange"))


# 12. **Sorting Tuples (Sortarea Tuplurilor):**
#     English: Create a tuple of numbers, then sort it in ascending order and print the result.
#     Romanian: Creați o tuplă de numere, apoi sortați-o în ordine crescătoare și tipăriți rezultatul.

number_tuple = (5, 1, 9, 3, 2, 7)
print(sorted(number_tuple))


# 13. **Nested Tuples (Tupluri Îngrădite):**
#     English: Create a nested tuple `nested_tuple` containing `my_tuple` and `other_tuple`, then print it.
#     Romanian: Creați o tuplă îngrădită `nested_tuple` care conține `my_tuple` și `other_tuple`, apoi tipăriți-o.

nested_tuple = (my_tuple, other_tuple)
print(nested_tuple)


# 14. **Converting Tuples (Conversia Tuplurilor):**
#     English: Convert `my_tuple` into a list and print the result.
#     Romanian: Convertiți `my_tuple` într-o listă și tipăriți rezultatul.

my_list = list(my_tuple)
print(my_list)


# 15. **Tuple Operations (Operații cu Tupluri):**
#     English: Perform the following operations:
#       - Concatenate `my_tuple` with itself.
#       - #       - Concatenate `my_tuple` with itself.
#       - Compare `my_tuple` with `other_tuple` using the greater than operator.
#     Romanian: Realizați următoarele operații:
#       - Concatenați `my_tuple` cu el însuși.
#       - Înmulțiți `my_tuple` cu 3.
#       - Comparați `my_tuple` cu `other_tuple` folosind operatorul mai mare decât.
#       Argumentati raspunsul, HINT:[["Hello"],["Salut"]]

# Concatenate `my_tuple` with itself.
new_tuple = my_tuple + my_tuple
print(new_tuple)

# Concatenate `my_tuple` with itself.
print(my_tuple * 3)

# Compare `my_tuple` with `other_tuple` using the greater than operator.
comparison = my_tuple > other_tuple
print(comparison)