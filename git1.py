'''Temperature Converter'''

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")
    print("Choose a conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        elif choice == 2:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
        else:
            print("Invalid choice. Please restart the program.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
