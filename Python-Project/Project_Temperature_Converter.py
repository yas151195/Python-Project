import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class Temperatureconverter:
    def __init__(self, temperature):
        self.temp = temperature

    def celcius_to_farenhite(self):
        farenhite = (self.temp * 9/5) + 32
        logging.info(f"Converted the {self.temp}F to {farenhite}C")
        return farenhite

    def farenhite_to_celcius(self):
        celcius = (self.temp -32) * 5/9
        logging.info(f"Converted the {celcius}C to {self.temp}F")
        return celcius

def convert_temperature():
    """Function to take input from the user and interact with the temparature"""
    print("Welcome to the Temperature Converter!")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice between (1-2): "))
        temperature = float(input("Enter the actual temperature to convert: "))

        # Create a object for the class
        converter = Temperatureconverter(temperature)

        if choice == 1:
            result = converter.celcius_to_farenhite()
            print(f"{temperature}C is the {result:.2f}F")

        elif choice == 2:
            result = converter.farenhite_to_celcius()
            print(f"{temperature}F is the {result:.2f}F")

        else:
            print("Envalid choice bro: chose exact value")

    except ValueError:
        logging.error("Invalid input. Please enter the number only.")
        print("Error: Plase enter valid numbers.")

if __name__ == "__main__":
    convert_temperature()
