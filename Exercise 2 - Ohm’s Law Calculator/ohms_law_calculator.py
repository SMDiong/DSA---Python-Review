# Diong, Shan Marc C.
# BSCpE 2-2
# September 24, 2024

# Exercise 2: Ohm’s Law Calculator
# Create a program that calculate Voltage, Current, or Resistance by using Ohm's Law

# Ask the user what they want to calculate. Either Voltage, Current, or Resistance
while True:
    print("\nWelcome to the Ohm's Law Calculator!")
    user_choice = input("Please enter 'V' to calculate Voltage,'I' for Current, and 'R' for Resistance: ")
# Ask the user to input values, Use Ohm's Law to calculate missing variable
    # Calculation for Voltage (V)
    if user_choice.upper() == 'V':
        print("\nCalculation for Voltage (V)")
        while True:
            try:
                current_value = float(input("Please enter the Current (I) in Amperes: "))
                resistance_value = float(input("Please enter the Resistance (R) in Ohms: "))
                if resistance_value == 0:
                    print("\nError! Resistance cannot be zero!\n")
                else:
                    voltage_value = current_value * resistance_value
                    print(f"The Voltage (V) is {voltage_value} volts")
                    break
            except ValueError:
                print("\nInvalid Input! Please enter numeric values!\n")

    # Calculation for Current (I)
    # Calculation for Resistance (R)

# Display Result

# End