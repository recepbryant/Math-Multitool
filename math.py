import curses
import math
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# ASCII art section
ascii_art = f"""
{Fore.LIGHTMAGENTA_EX}
                  77 65 84 72 64 77 85 76 84 73 84 79 79 76
 __  __    _  _____ _   _   ____  __  __ _   _ _   _____ ___ _____ ___   ___  _     
|  \/  |  / \|_   _| | | | / __ \|  \/  | | | | | |_   _|_ _|_   _/ _ \ / _ \| |    
| |\/| | / _ \ | | | |_| |/ / _` | |\/| | | | | |   | |  | |  | || | | | | | | |    
| |  | |/ ___ \| | |  _  | | (_| | |  | | |_| | |___| |  | |  | || |_| | |_| | |___ 
|_|  |_/_/   \_\_| |_| |_|\ \__,_|_|  |_|\___/|_____|_| |___| |_| \___/ \___/|_____|
                           \____/ b y   b r y a n t       .gg/Uz2T7we6pV                           
"""

# Function to display menu

def display_menu():
    print(ascii_art)
    print("Select the mathematical operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square root")
    print("8. Logarithm")
    print("9. Exponential")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Arcsine")
    print("14. Arccosine")
    print("15. Arctangent")
    print("16. Hyperbolic sine")
    print("17. Hyperbolic cosine")
    print("18. Hyperbolic tangent")
    print("19. Factorial")
    print("20. Ceiling")
    print("21. Floor")
    print("22. Absolute value")
    print("23. Pi")
    print("24. Euler's number (e)")
    print("25. Exit")

# Function to perform mathematical operations
def perform_operation(choice):
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", num1 + num2)
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", num1 - num2)
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", num1 * num2)
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", num1 / num2)
    elif choice == 5:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", num1 % num2)
    elif choice == 6:
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        print("Result:", math.pow(num1, num2))
    elif choice == 7:
        num = float(input("Enter a number: "))
        print("Square root:", math.sqrt(num))
    elif choice == 8:
        num = float(input("Enter a number: "))
        print("Logarithm:", math.log(num))
    elif choice == 9:
        num = float(input("Enter a number: "))
        print("Exponential:", math.exp(num))
    elif choice == 10:
        angle = float(input("Enter an angle in radians: "))
        print("Sine:", math.sin(angle))
    elif choice == 11:
        angle = float(input("Enter an angle in radians: "))
        print("Cosine:", math.cos(angle))
    elif choice == 12:
        angle = float(input("Enter an angle in radians: "))
        print("Tangent:", math.tan(angle))
    elif choice == 13:
        value = float(input("Enter a value: "))
        print("Arcsine:", math.asin(value))
    elif choice == 14:
        value = float(input("Enter a value: "))
        print("Arccosine:", math.acos(value))
    elif choice == 15:
        value = float(input("Enter a value: "))
        print("Arctangent:", math.atan(value))
    elif choice == 16:
        num = float(input("Enter a number: "))
        print("Hyperbolic sine:", math.sinh(num))
    elif choice == 17:
        num = float(input("Enter a number: "))
        print("Hyperbolic cosine:", math.cosh(num))
    elif choice == 18:
        num = float(input("Enter a number: "))
        print("Hyperbolic tangent:", math.tanh(num))
    elif choice == 19:
        num = int(input("Enter an integer: "))
        print("Factorial:", math.factorial(num))
    elif choice == 20:
        num = float(input("Enter a number: "))
        print("Ceiling:", math.ceil(num))
    elif choice == 21:
        num = float(input("Enter a number: "))
        print("Floor:", math.floor(num))
    elif choice == 22:
        num = float(input("Enter a number: "))
        print("Absolute value:", abs(num))
    elif choice == 23:
        print("Pi:", math.pi)
    elif choice == 24:
        print("Euler's number (e):", math.e)
    elif choice == 25:
        print("Exiting the program...")
        exit()
    else:
        print("Invalid choice!")

# Main program loop
while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-25): "))
        perform_operation(choice)
    except ValueError:
        print("Please enter a valid number.")
    choice = input("Select an option: \n1. Main Menu \n2. Exit\n")
    if choice == '1':
        continue
    elif choice == '3':
        print("Exiting the program...")
        exit()
    else:
        print("Invalid choice!")
