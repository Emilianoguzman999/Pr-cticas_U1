# PORTADA
# Nombre:    José Emiliano Guzmán Garza
# Matrícula: 2630535
# Grupo:     IM03
# Tema:      Manejo de números y booleanos en Python
# GitHub:    https://github.com/Emilianoguzman999/Pr-cticas_U1.git


# EXECUTIVE SUMMARY
# The int type stores whole numbers (age, hours, items_count) and the float
# type stores numbers with decimals (temperature, salary, bmi). The main
# difference is that a float can represent fractions and an int cannot.
# A boolean (True/False) is the result of a comparison, for example
# temp_c >= 30.0, and it can be combined with and, or, not to make decisions.
# It is important to validate ranges (no negative hours or salaries) and to
# avoid dividing by zero, because otherwise the program fails or gives wrong
# results. This document covers six problems, each with its description,
# inputs, outputs, validations and test cases, using ints, floats and
# booleans to make decisions.


# PRINCIPLES AND GOOD PRACTICES
# - Use appropriate types: int for counters, float for quantities with decimals.
# - Avoid duplicating complex expressions: save intermediate results in variables.
# - Validate data before operating (for example, hours and salaries not negative).
# - Use descriptive variable names and clear messages for the user.
# - Document how booleans are interpreted (what true and false mean in each case).


# Problem 1: Temperature converter and range flag
# Description: Converts a temperature in Celsius (float) to Fahrenheit and
# Kelvin. It also creates the boolean is_high_temperature, which is true if
# the Celsius temperature is greater than or equal to 30.0 and false otherwise.
#
# Inputs:
# - temp_c (float; temperature in Celsius)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
#
# Validations:
# - temp_c must be convertible to float.
# - Impossible temperatures are not allowed (temp_k < 0.0).
# - If something is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: temp_c = 35.0
#    -> Fahrenheit: 95.0, Kelvin: 308.15, High temperature: true
# 2) Border: temp_c = 30.0
#    -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
# 3) Error: temp_c = -300.0 (Kelvin would be negative) -> Error: invalid input
HIGH_TEMPERATURE_C = 30.0

valid_input = True
try:
    temp_c = float(input("Temperature in Celsius: "))
except ValueError:
    valid_input = False

if valid_input:
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        valid_input = False

if valid_input:
    is_high_temperature = temp_c >= HIGH_TEMPERATURE_C
    print("Fahrenheit:", temp_f)
    print("Kelvin:", temp_k)
    if is_high_temperature:
        print("High temperature: true")
    else:
        print("High temperature: false")
else:
    print("Error: invalid input")


# Problem 2: Work hours and overtime payment
# Description: Calculates the weekly pay of a worker. Up to 40 hours are paid
# at hourly_rate. Extra hours (more than 40) are paid at 150% of the normal
# rate. It also creates the boolean has_overtime, which is true if the worker
# did overtime.
#
# Inputs:
# - hours_worked (float; hours worked in the week)
# - hourly_rate (float; pay per hour)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false
#
# Validations:
# - hours_worked >= 0 and hourly_rate > 0.
# - Both values must be convertible to float.
# - If something is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: hours_worked = 45.0, hourly_rate = 100.0
#    -> Regular pay: 4000.0, Overtime pay: 750.0, Total pay: 4750.0,
#       Has overtime: true
# 2) Border: hours_worked = 40.0, hourly_rate = 100.0
#    -> Regular pay: 4000.0, Overtime pay: 0.0, Total pay: 4000.0,
#       Has overtime: false
# 3) Error: hours_worked = -5.0, hourly_rate = 100.0 -> Error: invalid input
REGULAR_HOURS = 40.0
OVERTIME_MULTIPLIER = 1.5

valid_input = True
try:
    hours_worked = float(input("Hours worked: "))
    hourly_rate = float(input("Hourly rate: "))
except ValueError:
    valid_input = False

if valid_input and (hours_worked < 0 or hourly_rate <= 0):
    valid_input = False

if valid_input:
    regular_hours = min(hours_worked, REGULAR_HOURS)
    overtime_hours = max(hours_worked - REGULAR_HOURS, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS

    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    if has_overtime:
        print("Has overtime: true")
    else:
        print("Has overtime: false")
else:
    print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
# Description: Determines if a customer gets a discount. The customer gets it
# if is_student is true OR is_senior is true OR purchase_total >= 1000.0.
# It also calculates the final total, applying a 10% discount when eligible.
#
# Inputs:
# - purchase_total (float; total of the purchase)
# - is_student_text (string; "YES" or "NO")
# - is_senior_text (string; "YES" or "NO")
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0 and convertible to float.
# - The texts are converted to uppercase and then to booleans is_student and
#   is_senior.
# - If a text is not "YES" or "NO", "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: purchase_total = 500.0, is_student_text = "YES", is_senior_text = "NO"
#    -> Discount eligible: true, Final total: 450.0
# 2) Border: purchase_total = 1000.0, is_student_text = "NO", is_senior_text = "NO"
#    -> Discount eligible: true, Final total: 900.0
# 3) Error: purchase_total = 300.0, is_student_text = "MAYBE", is_senior_text = "NO"
#    -> Error: invalid input
MIN_DISCOUNT_TOTAL = 1000.0
DISCOUNT_FACTOR = 0.9

valid_input = True
try:
    purchase_total = float(input("Purchase total: "))
except ValueError:
    valid_input = False
is_student_text = input("Is student (YES/NO): ").strip().upper()
is_senior_text = input("Is senior (YES/NO): ").strip().upper()

if valid_input and purchase_total < 0.0:
    valid_input = False
if is_student_text != "YES" and is_student_text != "NO":
    valid_input = False
if is_senior_text != "YES" and is_senior_text != "NO":
    valid_input = False

if valid_input:
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"
    discount_eligible = is_student or is_senior or (purchase_total >= MIN_DISCOUNT_TOTAL)
    if discount_eligible:
        final_total = purchase_total * DISCOUNT_FACTOR
        print("Discount eligible: true")
    else:
        final_total = purchase_total
        print("Discount eligible: false")
    print("Final total:", final_total)
else:
    print("Error: invalid input")


# Problem 4: Basic statistics of three integers
# Description: Reads three integers and calculates the sum, the average
# (float), the maximum value, the minimum value and the boolean all_even,
# which is true if the three numbers are even.
#
# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
#
# Validations:
# - The three values must be convertible to int.
# - No other restrictions (negative numbers are allowed).
# - If something is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: n1 = 4, n2 = 8, n3 = 10
#    -> Sum: 22, Average: 7.333333333333333, Max: 10, Min: 4, All even: true
# 2) Border: n1 = -3, n2 = 0, n3 = 3 (negatives and zero)
#    -> Sum: 0, Average: 0.0, Max: 3, Min: -3, All even: false
# 3) Error: n1 = "x", n2 = 2, n3 = 3 -> Error: invalid input
valid_input = True
try:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
except ValueError:
    valid_input = False

if valid_input:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    if all_even:
        print("All even: true")
    else:
        print("All even: false")
else:
    print("Error: invalid input")


# Problem 5: Loan eligibility (income and debt ratio)
# Description: Determines if a person is eligible for a loan using
# monthly_income (float), monthly_debt (float) and credit_score (int).
# debt_ratio = monthly_debt / monthly_income. The person is eligible if
# monthly_income >= 8000.0 AND debt_ratio <= 0.4 AND credit_score >= 650.
#
# Inputs:
# - monthly_income (float; monthly income)
# - monthly_debt (float; monthly debt payments)
# - credit_score (int; credit score)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
#
# Validations:
# - monthly_income > 0.0 (avoids division by zero).
# - monthly_debt >= 0.0 and credit_score >= 0.
# - The values must be convertible to float or int as needed.
# - If something is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: monthly_income = 10000.0, monthly_debt = 3000.0, credit_score = 700
#    -> Debt ratio: 0.3, Eligible: true
# 2) Border: monthly_income = 8000.0, monthly_debt = 3200.0, credit_score = 650
#    -> Debt ratio: 0.4, Eligible: true
# 3) Error: monthly_income = 0.0, monthly_debt = 500.0, credit_score = 700
#    -> Error: invalid input
MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

valid_input = True
try:
    monthly_income = float(input("Monthly income: "))
    monthly_debt = float(input("Monthly debt: "))
    credit_score = int(input("Credit score: "))
except ValueError:
    valid_input = False

if valid_input and (monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0):
    valid_input = False

if valid_input:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_INCOME and debt_ratio <= MAX_DEBT_RATIO and credit_score >= MIN_CREDIT_SCORE)

    print("Debt ratio:", debt_ratio)
    if eligible:
        print("Eligible: true")
    else:
        print("Eligible: false")
else:
    print("Error: invalid input")


# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates the body mass index with bmi = weight_kg /
# (height_m * height_m). It also creates the booleans is_underweight
# (bmi < 18.5), is_normal (18.5 <= bmi < 25.0) and is_overweight (bmi >= 25.0).
#
# Inputs:
# - weight_kg (float; weight in kilograms)
# - height_m (float; height in meters)
#
# Outputs:
# - "BMI:" <rounded_bmi>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
#
# Validations:
# - weight_kg > 0.0 and height_m > 0.0 (this also avoids division by zero).
# - Both values must be convertible to float.
# - If something is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: weight_kg = 70.0, height_m = 1.75
#    -> BMI: 22.86, Underweight: false, Normal: true, Overweight: false
# 2) Border: weight_kg = 74.0, height_m = 2.0 (bmi is exactly 18.5)
#    -> BMI: 18.5, Underweight: false, Normal: true, Overweight: false
# 3) Error: weight_kg = 70.0, height_m = 0.0 -> Error: invalid input
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0

valid_input = True
try:
    weight_kg = float(input("Weight in kg: "))
    height_m = float(input("Height in meters: "))
except ValueError:
    valid_input = False

if valid_input and (weight_kg <= 0.0 or height_m <= 0.0):
    valid_input = False

if valid_input:
    bmi = weight_kg / (height_m * height_m)
    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT

    print("BMI:", round(bmi, 2))
    if is_underweight:
        print("Underweight: true")
    else:
        print("Underweight: false")
    if is_normal:
        print("Normal: true")
    else:
        print("Normal: false")
    if is_overweight:
        print("Overweight: true")
    else:
        print("Overweight: false")
else:
    print("Error: invalid input")


# CONCLUSIONS
# Integers and floats work together in real calculations, like using int hours
# or scores with float rates, salaries and ratios. Comparisons generate
# booleans, and those booleans let us make decisions with if. Validating ranges
# and avoiding divisions by zero prevented errors and wrong results in every
# problem. I learned that combined conditions with and, or, not must be
# written carefully to follow the rule exactly. These patterns repeat in
# payroll, discounts, loans and health calculations.


# REFERENCES
# References:
# 1) Python documentation - Numeric and Boolean types
# 2) Python documentation - Boolean operations: and, or, not
# 3) Python documentation - Comparisons (relational operators)
# 4) Python documentation - Built-in Functions: int, float, bool, round, abs, min, max
# 5) Class notes and official resources of the course
