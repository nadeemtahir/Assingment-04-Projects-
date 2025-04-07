gravity_of_all_planets = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0,
}

def planetary_weight_calculator():
    # Input: Weight on Earth
    while True:
        try:
            earth_weight = float(input("Enter your weight on Earth (in kg): "))
            if earth_weight <= 0:
                print("Weight must be a positive value. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Input: Planet Name
    while True:
        planet = input("Enter a planet name (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ").capitalize()
        if planet in gravity_of_all_planets:
            break
        else:
            print("Invalid planet name. Please enter a valid planet from the list.")

    # Retrieve Gravity for the Selected Planet
    gravity = gravity_of_all_planets[planet]

    # Calculate Weight on Selected Planet
    planetary_weight = earth_weight * gravity / 100
    rounded_planetary_weight = round(planetary_weight, 2)

    # Output the result
    print(f"\nYour weight on {planet}: {rounded_planetary_weight} kg")

# Run the function
planetary_weight_calculator()
