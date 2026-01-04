# Ask the user for temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = celsius * 9/5 + 32
# Print the temperature in Fahrenheit
print(f"Temperature in Fahrenheit: {fahrenheit}°F")
# Give advice based on Celsius temperature
if celsius < 0:
    print("Very cold! Wear thick jacket")
elif 0 <= celsius <= 15:
    print("Cold. Wear jacket")
elif 16 <= celsius <= 25:
    print("Nice weather")
else:  # celsius > 25
    print("Hot! Stay hydrated")
