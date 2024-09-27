# Diong, Shan Marc C.
# BSCpE 2-2
# September 24, 2024

# Exercise 2: Ohm’s Law Calculator
# Create a program that calculate Voltage, Current, or Resistance by using Ohm's Law

#  Word Colors
green = "\033[0;32m"
blue = "\033[0;34m"
yellow = "\033[1;33m"
red = "\033[0;31m"

# Ask the user what they want to calculate. Either Voltage, Current, or Resistance
print(green + "\nWelcome to the Ohm's Law Calculator!")
while True:
    user_choice = input(green + f"\nPlease enter {blue + "'V'" + green} to calculate Voltage,{blue + "'I'" + green} for Current, and {blue + "'R'" + green} for Resistance: ")

    # Ask the user to input values, Use Ohm's Law to calculate missing variable and display results
    # Calculation for Voltage (V)
    if user_choice.upper() == 'V':
        print(blue + "\nCalculation for Voltage (V) = Current (I) x Resistance (R)" + green)
        while True:
            try:
                current_value = float(input("Please enter the Current (I) in Amperes: "))
                resistance_value = float(input("Please enter the Resistance (R) in Ω: "))
                voltage_value = current_value * resistance_value
                print(yellow + f"\nThe Voltage (V) is {voltage_value} volts" + green)
                break
            except ValueError:
                print(red + "\nInvalid Input! Please enter numeric values!\n" + green)

    # Calculation for Current (I)
    elif user_choice.upper() == 'I':
        print(blue + "\nCalculation for Current (I) = Voltage (V) ÷ Resistance (R)" + green)
        while True:
            try:
                voltage_value = float(input("Please enter the Voltage (V) in Volts: "))
                resistance_value = float(input("Please enter the Resistance (R) in Ω: "))
                if resistance_value == 0:
                    print(red + "\nError! Division cannot be zero!\n" + green)
                elif voltage_value == 0:
                    print(red + "\nError! Division cannot be zero!\n" + green)
                else:
                    current_value = voltage_value / resistance_value
                    print(yellow + f"\nThe Current (I) is {current_value} Amperes" + green)
                    break
            except ValueError:
                print(red + "\nInvalid Input! Please enter numeric values!\n" + green)

    # Calculation for Resistance (R)
    elif user_choice.upper() == 'R':
        print(blue + "\nCalculations for Resistance (R) = Voltage (V) ÷ Current (I)" + green)
        while True:
            try:
                voltage_value = float(input("Please enter the Voltage (V) in Volts: "))
                current_value = float(input("Please enter the Current (I) in Amperes: "))
                if current_value == 0:
                    print(red + "\nError! Division cannot be zero!\n" + green)
                elif voltage_value == 0:
                    print(red + "\nError! Division cannot be zero!\n" + green)
                else:
                    resistance_value = voltage_value / current_value
                    print(yellow + f"\nThe Resistance (R) is {resistance_value} Ω" + green)
                    break
            except ValueError:
                print(red + "\nInvalid Input! Please enter numeric values!\n" + green)

    # Invalid Inputs
    else:
        print(red + "\nInvalid Input!" + green)

    # Ask if the user wants to try again
    while True:
        try_again = input(green + "\nDo you want to try again? (Y/N): " + green).strip().upper()
        if try_again == 'Y':
            break
        elif try_again == 'N':
            print(blue + "\nThank you for using the program!" + green)
            exit()
        else:
            print(red + "\nInvalid input! Please enter 'Y' or 'N'." + green)
# End