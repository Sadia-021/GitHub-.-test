# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

# Main program
def temperature_converter():
    print("Temperature Converter")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    
    # Take user choice as input
    choice = input("Enter your choice (1 or 2): ")
    
    # Perform the conversion based on user choice
    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius")
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit")
    else:
        print("Invalid choice! Please select either 1 or 2.")
