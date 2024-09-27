# Diong, Shan Marc C.
# BSCpE 2-2
# September 24, 2024

# Exercise 3: Diamond Shape
# Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.

# Word Colors
green = "\033[0;32m"
blue = "\033[0;34m"
yellow = "\033[1;33m"
red = "\033[0;31m"


# Function for printing a diamond pattern of width n using '*' characters.
def print_diamond(n):
    # Checker if n is odd
    if n % 2 == 0:
        return red + "Invalid Input! Please input an odd integer" + green

    # Prints the top part of the diamond
    for i in range(1, n + 1, 2):
        diamond_space = (n - i) // 2
        print(yellow + ' ' * diamond_space + '*' * i)

    # Prints the bottom part of the diamond
    for i in range(n - 2, 0, -2):
        diamond_space = (n - i) // 2
        print(' ' * diamond_space + '*' * i)


# Main Function
def main():
    while True:
        # Ask the user for input of odd integer n
        # Example usage n = 5
        try:
            n = int(input(green + "\nPlease enter an odd integer for the diamond's width (n): "))
            print("\n")
            diamond = print_diamond(n)
            if diamond:
                print(diamond)
        except ValueError:
            print(red + "Invalid Input! Please enter a valid integer" + green)

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


main()

# End