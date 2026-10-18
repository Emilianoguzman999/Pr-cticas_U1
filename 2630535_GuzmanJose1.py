#PORTADA
# Manejo de Listas, Tuplas y Diccionarios en Python
# Name:       Jose Emiliano Guzman Garza
# Matricula:  2630535
# Grupo:      IM03

# EXECUTIVE SUMMARY
# A list is an ordered collection of elements written with square brackets.
# A tuple is also ordered but it is written with parentheses and cannot be
# changed after it is created. A dictionary stores key-value pairs and lets us
# find a value using its key. A list is mutable: we can add, remove or change
# its elements. A tuple is immutable: its elements stay fixed. Dictionaries
# associate a key (name, id, code) with a value (price, phone, grades list).
# This document covers six problems, each with its description, inputs,
# outputs, validations and test cases, using lists, tuples and dictionaries in
# practical contexts such as catalogs, records and statistics.

# PRINCIPLES AND GOOD PRACTICES
# - Use lists when you need to add or remove elements frequently.
# - Use tuples for data that must not change (coordinates, dates, fixed settings).
# - Use dictionaries when you need to look up information by a key (name, id, code).
# - Avoid modifying a list while looping over it with a for loop.
# - Use descriptive key names in dictionaries ("name", "age", "price").
# - Write readable code and clear messages for the user.


# Problem 1: Shopping list basics (list operations)
# Description: Builds a list of items from a comma-separated text, adds a new
# item at the end, shows the total number of items and checks if a specific
# item is in the list.

# Inputs:
# - initial_items_text (string, e.g. "apple,banana,orange")
# - new_item (string)
# - search_item (string)

# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false

# Validations:
# - initial_items_text, new_item and search_item are not empty after strip().
# - The text is split by commas and extra spaces are removed from each item.
# - Decision: an empty initial list (blank text) is not allowed, it is an error.

# Test cases:
# 1) Normal: "apple,banana,orange", new_item "grape", search_item "banana"
#    -> Items list: ['apple', 'banana', 'orange', 'grape'], Total items: 4,
#       Found item: true
# 2) Border: " apple ", new_item "milk", search_item "bread"
#    -> Items list: ['apple', 'milk'], Total items: 2, Found item: false
# 3) Error: initial_items_text = "   " -> Error: invalid input
initial_items_text = input("Initial items (comma separated): ").strip()
new_item = input("New item to add: ").strip()
search_item = input("Item to search: ").strip()

if initial_items_text == "" or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list = initial_items_text.split(",")
    for i in range(len(items_list)):
        items_list[i] = items_list[i].strip()
    items_list.append(new_item)
    len_list = len(items_list)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", len_list)
    if is_in_list:
        print("Found item: true")
    else:
        print("Found item: false")



# Problem 2: Points and distances with tuples
# Description: Creates two points of a 2D plane as tuples, calculates the
# Euclidean distance between them and creates a new tuple with the midpoint.

# Inputs:
# - x1, y1, x2, y2 (float)

# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)

# Validations:
# - The 4 inputs must be convertible to float.

# Test cases:
# 1) Normal: x1=0, y1=0, x2=3, y2=4
#    -> Point A: (0.0, 0.0), Point B: (3.0, 4.0), Distance: 5.0,
#       Midpoint: (1.5, 2.0)
# 2) Border: x1=2, y1=2, x2=2, y2=2 (same point)
#    -> Distance: 0.0, Midpoint: (2.0, 2.0)
# 3) Error: x1="abc" -> Error: invalid input
valid_numbers = True
try:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
except ValueError:
    valid_numbers = False

if valid_numbers:
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
else:
    print("Error: invalid input")


# Problem 3: Product catalog with dictionary
# Description: Uses a dictionary as a catalog (product name -> unit price).
# Reads a product name and a quantity and calculates the total to pay if the
# product exists. If it does not exist, it shows an error message.

# Inputs:
# - product_name (string)
# - quantity (int)

# Outputs:
# - If the product exists: "Unit price:" <unit_price>, "Quantity:" <quantity>,
#   "Total:" <total_price>
# - If it does not exist: "Error: product not found"

# Validations:
# - quantity must be an int and quantity > 0.
# - product_name is not empty after strip().
# - product_name must be a key of the dictionary.

# Test cases:
# 1) Normal: product_name "apple", quantity 3
#    -> Unit price: 10.0, Quantity: 3, Total: 30.0
# 2) Border: product_name "milk", quantity 1
#    -> Unit price: 22.5, Quantity: 1, Total: 22.5
# 3) Error: product_name "pizza", quantity 2 -> Error: product not found
product_prices = {"apple": 10.0, "banana": 8.5, "milk": 22.5}

product_name = input("Product name: ").strip()
valid_quantity = True
try:
    quantity = int(input("Quantity: "))
except ValueError:
    valid_quantity = False

if product_name == "" or valid_quantity == False:
    print("Error: invalid input")
elif quantity <= 0:
    print("Error: invalid input")
elif product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)
else:
    print("Error: product not found")


# Problem 4: Student grades with dict and list
# Description: Uses a dictionary where the key is the student name and the
# value is a list of grades. Reads a student name, calculates the average of
# the grades and tells if the student passed (average >= 70.0).

# Inputs:
# - student_name (string)

# Outputs:
# - If the student exists: "Grades:" <grades_list>, "Average:" <average>,
#   "Passed:" true|false
# - If the student does not exist: "Error: student not found"

# Validations:
# - student_name is not empty after strip().
# - student_name must be a key of the dictionary.
# - The grades list must not be empty before calculating the average.

# Test cases:
# 1) Normal: student_name "Alice"
#    -> Grades: [90.0, 85.0], Average: 87.5, Passed: true
# 2) Border: student_name "Carlos" (average exactly 70.0)
#    -> Grades: [70.0, 70.0], Average: 70.0, Passed: true
# 3) Error: student_name "Zoe" -> Error: student not found
grades = {
    "Alice": [90.0, 85.0],
    "Bob": [60.0, 55.0, 70.0],
    "Carlos": [70.0, 70.0],
}

student_name = input("Student name: ").strip()

if student_name == "":
    print("Error: invalid input")
elif student_name in grades:
    grades_list = grades[student_name]
    if len(grades_list) == 0:
        print("Error: invalid input")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", average)
        if is_passed:
            print("Passed: true")
        else:
            print("Passed: false")
else:
    print("Error: student not found")


# Problem 5: Word frequency counter (list + dict)
# Description: Reads a sentence, converts it to lowercase and splits it into a
# list of words. Then builds a dictionary with the frequency of each word and
# shows it with the most frequent word.
#
# Inputs:
# - sentence (string)

# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word> (if there is a tie, the first one found is used)
#
# Validations:
# - sentence is not empty after strip().
# - Decision: simple punctuation (. , ; : ! ?) is removed with replace().
# - The words list must not be empty.

# Test cases:
# 1) Normal: "The cat and the dog."
#    -> Words list: ['the', 'cat', 'and', 'the', 'dog'],
#       Frequencies: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1},
#       Most common word: the
# 2) Border: "Hello"
#    -> Words list: ['hello'], Frequencies: {'hello': 1},
#       Most common word: hello
# 3) Error: "   " -> Error: invalid input
sentence = input("Sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    clean_sentence = sentence.lower()
    clean_sentence = clean_sentence.replace(".", "")
    clean_sentence = clean_sentence.replace(",", "")
    clean_sentence = clean_sentence.replace(";", "")
    clean_sentence = clean_sentence.replace(":", "")
    clean_sentence = clean_sentence.replace("!", "")
    clean_sentence = clean_sentence.replace("?", "")
    words_list = clean_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        highest_count = 0
        for word in freq_dict:
            if freq_dict[word] > highest_count:
                highest_count = freq_dict[word]
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# Problem 6: Simple contact book (dictionary CRUD)
# Description: Uses a dictionary as a contact book (name -> phone). Reads an
# action (ADD, SEARCH or DELETE) and applies it to the dictionary, then shows
# a message with the result of the operation.

# Inputs:
# - action_text (string: "ADD", "SEARCH" or "DELETE")
# - name (string)
# - phone (string, only for "ADD")

# Outputs:
# - ADD: "Contact saved:" name, phone
# - SEARCH: "Phone:" <phone> or "Error: contact not found"
# - DELETE: "Contact deleted:" name or "Error: contact not found"

# Validations:
# - action_text is converted to uppercase and must be ADD, SEARCH or DELETE.
# - name is not empty after strip().
# - For "ADD", phone is not empty after strip().

# Test cases:
# 1) Normal: action_text "ADD", name "Eva", phone "8112345678"
#    -> Contact saved: Eva 8112345678
# 2) Border: action_text "add" (lowercase), name "Alice", phone "999"
#    -> Contact saved: Alice 999 (the existing contact is updated)
# 3) Error: action_text "SEARCH", name "Nobody" -> Error: contact not found
contacts = {"Alice": "1234567890", "Bob": "5551234567", "Carlos": "8180001111"}

action_text = input("Action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text != "ADD" and action_text != "SEARCH" and action_text != "DELETE":
    print("Error: invalid input")
else:
    name = input("Name: ").strip()
    if name == "":
        print("Error: invalid input")
    elif action_text == "ADD":
        phone = input("Phone: ").strip()
        if phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts.get(name))
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


# CONCLUSIONS
# Lists are best when the data changes, because we can add and remove elements
# with append() and remove() in a flexible way. Tuples are useful for data that
# must not change, like the coordinates of a point. Dictionaries make it easy
# to find information quickly by its key, like a price or a phone number.
# A common pattern was combining structures, for example a dictionary of lists
# (student -> grades) or a list used to build a dictionary of frequencies.
# Validating the inputs first avoided errors like empty lists or missing keys.

# REFERENCES
# References:
# 1) Python documentation - Built-in Types: list, tuple, dict
# 2) Python documentation - The Python Tutorial: Data Structures
# 3) Python documentation - Built-in Functions: len, sum, min, max, sorted
# 4) Python documentation - Built-in Types: string methods (strip, split, lower, upper, replace)
# 5) Class notes and official resources of the course

