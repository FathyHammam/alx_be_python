# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_FAHRENHEIT = 32  # Freezing point of water in Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Convert the temperature from Fahrenheit to Celsius using the global conversion factor
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Convert the temperature from Celsius to Fahrenheit using the global conversion factor
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FREEZING_POINT_FAHRENHEIT

# Main function to interact with the user
def main():
    try:
 
