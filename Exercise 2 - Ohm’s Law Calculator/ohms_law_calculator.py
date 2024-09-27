# Diong, Shan Marc C.
# BSCpE 2-2
# September 24, 2024

# Exercise 2: Ohm’s Law Calculator
# Create a program that calculate Voltage, Current, or Resistance by using Ohm's Law

# Ask the user what they want to calculate. Either Voltage, Current, or Resistance
print("\nWelcome to the Ohm's Law Calculator!")
while True:
    user_choice = input("Please enter 'V' to calculate Voltage,'I' for Current, and 'R' for Resistance: ")

# Ask the user to input values, Use Ohm's Law to calculate missing variable and display results
    # Calculation for Voltage (V)
    if user_choice.upper() == 'V':
        print("\nCalculation for Voltage (V)")
        while True:
            try:
                current_value = float(input("Please enter the Current (I) in Amperes: "))
                resistance_value = float(input("Please enter the Resistance (R) in Ω: "))
                voltage_value = current_value * resistance_value
                print(f"\nThe Voltage (V) is {voltage_value} volts")
                break
            except ValueError:
                print("\nInvalid Input! Please enter numeric values!\n")

    # Calculation for Current (I)
    elif user_choice.upper() == 'I':
        print("\nCalculation for Current (I)")
        while True:
            try:
                voltage_value = float(input("Please enter the Voltage (V) in Volts: "))
                resistance_value = float(input("Please enter the Resistance (R) in Ω: "))
                if resistance_value == 0:
                    print("\nError! Division cannot be zero!\n")
                else:
                    current_value = voltage_value / resistance_value
                    print(f"\nThe Current (I) is {current_value} Amperes")
                    break
            except ValueError:
                print("\nInvalid Input! Please enter numeric values!\n")

    # Calculation for Resistance (R)
    elif user_choice.upper() == 'R':
        print("\nCalculations for Resistance (R)")
        while True:
            try:
                voltage_value = float(input("Please enter the Voltage (V) in Volts: "))
                current_value = float(input("Please enter the Current (I) in Amperes: "))
                if current_value == 0:
                    print("\nError! Division cannot be zero!\n")
                else:
                    resistance_value = voltage_value / current_value
                    print(f"The Resistance (R) is {resistance_value} Ω")
                    break
            except ValueError:
                print("\nInvalid Input! Please enter numeric values!\n")

    else:
        print("\nInvalid Input!\n")
# End