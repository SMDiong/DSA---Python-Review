# Diong, Shan Marc C.
# BSCpE 2-2
# September 24, 2024

# Exercise 1: Temperature Converter
# Create a program that converts temperatures between Celsius and Fahrenheit.

# Ask the user for input of temperature
print("Welcome to the Temperature Converter!")
temp_value = float(input("Please input the value of the Temperature: "))

# Ask the user to select conversion type from Celsius to Fahrenheit or from Fahrenheit to Celsius
print("\nPlease select a conversion type")
conversion_type = input("Type 'C' to convert from Celsius to Fahrenheit or type 'F' to convert from Fahrenheit to Celsius: ")

# Conversion and Output result
if conversion_type.upper() == 'C':
    # Celsius to Fahrenheit
    converted_celsius = (temp_value * 9/5) + 32
    print(f"\n{temp_value}° Celsius is {converted_celsius}° Fahrenheit.")
elif conversion_type.upper() == 'F':
    # Fahrenheit to Celsius
    converted_fahrenheit = (temp_value -32) * 5/9
    print(f"\n{temp_value}° Fahrenheit is {converted_fahrenheit}° Celsius.")
else:
    # Invalid Input
    print("\nInvalid Input! Please type 'C' or 'F'.")

# End