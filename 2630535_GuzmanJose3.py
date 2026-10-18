# PORTADA
# Name: José Emiliano Guzmán Garza
# Student ID: 2630535
# Group: IM03
# Topic: String Handling in Python
# GitHub Repository: https://github.com/Emilianoguzman999/Pr-cticas_U1.git

# EXECUTIVE SUMMARY
# A string is a Python data type used to store text as a sequence of characters.
# Strings are immutable, which means their characters cannot be changed in place.
# Python supports operations such as concatenation, length calculation, indexing, slicing,
# searching, replacing, splitting, joining, and formatting text.
# Validating and normalizing input helps prevent errors and keeps names, emails, and other
# user-provided data consistent before the program processes it.
# This document contains six practical string-handling problems with descriptions,
# inputs, outputs, validations, and normal, border, and error test cases.
# Each problem includes executable Python code and uses built-in string methods where useful.

# PRINCIPLES AND GOOD PRACTICES
# - Strings are immutable: any transformation creates and returns a new string.
# - Normalize input with strip() and, when appropriate, lower() before comparisons.
# - Avoid unexplained magic numbers in slices; document the range being extracted.
# - Use built-in string methods instead of rewriting basic text-processing logic.
# - Validate input in clear steps: check that it is not empty, then check its format.
# - Use descriptive variable names and understandable error messages.

# Problem 1: Full Name Formatter
# Description:
# Reads a full name, removes extra spaces, and formats each word in title case.
# It also creates uppercase initials separated by periods.
#
# Inputs:
# - full_name_input: a full name that may contain mixed casing or extra spaces.
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - The input must not be empty after strip().
# - The full name must contain at least two words.
#
# Test cases:
# 1) Normal: "  juan carlos tovar  " -> "Juan Carlos Tovar", initials "J.C.T."
# 2) Border: "a b" -> "A B", initials "A.B."
# 3) Error: "   juan   " -> "Error: invalid input"

full_name_input = input("Enter full name: ").strip()
name_words = full_name_input.split()

if len(name_words) < 2:
    print("Error: invalid input")
else:
    formatted_name = " ".join(name_words).title()
    initials = ".".join(word[0].upper() for word in name_words) + "."
    print("Formatted name:", formatted_name)
    print("Initials:", initials)

# Problem 2: Simple Email Validator
# Description:
# Checks a basic email structure and extracts the domain when the address is valid.
# A valid address must contain exactly one '@', a dot after '@', and no whitespace.
#
# Inputs:
# - email_text: a candidate email address.
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - "Domain: <domain_part>" when valid.
#
# Validations:
# - The input must not be empty after strip().
# - The address must contain exactly one '@'.
# - The address must not contain whitespace.
# - The domain must contain a dot and must not start or end with a dot.
#
# Test cases:
# 1) Normal: "user@example.com" -> valid, domain "example.com"
# 2) Border: "a@b.c" -> valid, domain "b.c"
# 3) Error: "user @example.com" -> "Valid email: false"

email_text = input("Enter email address: ").strip()
email_is_valid = True

if not email_text or any(character.isspace() for character in email_text):
    email_is_valid = False
elif email_text.count("@") != 1:
    email_is_valid = False

if email_is_valid:
    at_index = email_text.find("@")
    local_part = email_text[:at_index]
    domain_part = email_text[at_index + 1:]
    if (not local_part or not domain_part or "." not in domain_part
            or domain_part.startswith(".") or domain_part.endswith(".")):
        email_is_valid = False

if email_is_valid:
    print("Valid email: true")
    print("Domain:", domain_part)
else:
    print("Valid email: false")

# Problem 3: Palindrome Checker
# Description:
# Determines whether a phrase reads the same forward and backward.
# The comparison ignores spaces and letter casing.
#
# Inputs:
# - phrase_input: a phrase or sentence.
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - "Normalized text: <cleaned_text>"
#
# Validations:
# - The input must not be empty after strip().
# - The normalized text must contain at least three characters.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> palindrome
# 2) Border: "Aba" -> palindrome
# 3) Error: "   hi   " -> "Error: invalid input"

phrase_input = input("Enter phrase: ").strip()
cleaned_phrase = phrase_input.lower().replace(" ", "")

if not phrase_input or len(cleaned_phrase) < 3:
    print("Error: invalid input")
else:
    is_palindrome = cleaned_phrase == cleaned_phrase[::-1]
    print("Normalized text:", cleaned_phrase)
    print("Is palindrome:", str(is_palindrome).lower())

# Problem 4: Sentence Word Statistics
# Description:
# Splits a sentence into words and calculates the total word count.
# It also displays the first, last, shortest, and longest words.
#
# Inputs:
# - sentence_input: a sentence to analyze.
#
# Outputs:
# - "Word count: <n>"
# - "First word: <word>"
# - "Last word: <word>"
# - "Shortest word: <word>"
# - "Longest word: <word>"
#
# Validations:
# - The sentence must not be empty after strip().
# - The sentence must contain at least one word after split().
#
# Test cases:
# 1) Normal: "Python is an amazing programming language" -> 6 words;
#    first "Python", last "language", shortest "is", longest "programming".
# 2) Border: "   Hello   " -> 1 word; first, last, shortest, and longest are "Hello".
# 3) Error: "     " -> "Error: invalid input"

sentence_input = input("Enter sentence: ").strip()
sentence_words = sentence_input.split()

if not sentence_words:
    print("Error: invalid input")
else:
    word_count = len(sentence_words)
    first_word = sentence_words[0]
    last_word = sentence_words[-1]
    shortest_word = min(sentence_words, key=len)
    longest_word = max(sentence_words, key=len)

    print("Word count:", word_count)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)

# Problem 5: Password Strength Classifier
# Description:
# Classifies a password as weak, medium, or strong using its length and character types.
# Strong passwords need at least eight characters, uppercase and lowercase letters,
# a digit, and a non-alphanumeric symbol.
#
# Inputs:
# - password_input: the password to evaluate.
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - The password must not be empty.
# - The password length is checked with len().
#
# Test cases:
# 1) Normal: "P@ssword123" -> "Password strength: strong"
# 2) Border: "Pass1234" -> "Password strength: medium"
# 3) Error: "" -> "Error: invalid input"
#
# Classification rules:
# - Strong: length >= 8 and uppercase, lowercase, digit, and symbol are all present.
# - Medium: length >= 8 and at least two of the character categories are present.
# - Weak: shorter than 8 characters or fewer than two character categories are present.

password_input = input("Enter password: ")

if not password_input:
    print("Error: invalid input")
else:
    password_length = len(password_input)
    has_upper = any(character.isupper() for character in password_input)
    has_lower = any(character.islower() for character in password_input)
    has_digit = any(character.isdigit() for character in password_input)
    has_symbol = any(not character.isalnum() for character in password_input)

    category_count = sum((has_upper, has_lower, has_digit, has_symbol))

    if (password_length >= 8 and has_upper and has_lower
            and has_digit and has_symbol):
        password_strength = "strong"
    elif password_length >= 8 and category_count >= 2:
        password_strength = "medium"
    else:
        password_strength = "weak"

    print("Password strength:", password_strength)

# Problem 6: Product Label Formatter
# Description:
# Creates a product label containing the product name and its price.
# The final label is exactly 30 characters long: it is cropped if too long
# or padded with spaces on the right if it is too short.
#
# Inputs:
# - product_name: the product name.
# - price_input: a string that must be convertible to a positive number.
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'
#
# Validations:
# - The product name must not be empty after strip().
# - The price must convert to a number greater than zero.
#
# Test cases:
# 1) Normal: product "Coffee", price "4.50" -> a 30-character label.
# 2) Border: product "Super Ultra Mega Product Name", price "100.00"
#    -> label cropped to the first 30 characters.
# 3) Error: product "Milk", price "-5.00" -> "Error: invalid input"

product_name = input("Enter product name: ").strip()
price_input = input("Enter price: ").strip()

try:
    price_value = float(price_input)
    price_is_valid = price_value > 0
except ValueError:
    price_is_valid = False
    price_value = 0.0

if not product_name or not price_is_valid:
    print("Error: invalid input")
else:
    raw_label = f"Product: {product_name} | Price: ${price_value:g}"
    formatted_label = raw_label[:30].ljust(30)
    print(f'Label: "{formatted_label}"')

# CONCLUSIONS
# String handling is important because programs often need to read, check, and display text.
# strip() removes extra spaces at the beginning and end, while lower() helps compare text
# without treating uppercase and lowercase letters as different.
# split() separates a sentence into words, and join() combines words into a single string.
# Input validation helps prevent empty values, invalid formats, and incorrect data from
# being processed as if it were valid.
# Since strings are immutable, methods such as replace() return a new string instead
# of changing the original one.
# Slicing, such as text[::-1] or label[:30], makes it possible to extract or reverse text.
# These exercises demonstrate how clear validation and built-in methods make code easier
# to read, test, and maintain.

# REFERENCES
# 1) Python Documentation - Built-in Types: Text Sequence Type — str:
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Documentation - Common String Operations:
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Documentation - Input and Output:
#    https://docs.python.org/3/tutorial/inputoutput.html
# 4) W3Schools - Python Strings:
#    https://www.w3schools.com/python/python_strings.asp
# 5) Real Python - Python String Formatting:
#    https://realpython.com/python-f-strings/
# 6) Course notes - Basic Algorithms and Python Programming.
