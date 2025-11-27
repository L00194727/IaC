# List of 10 temperatures in Kelvin
temps_kelvin = [250, 260, 270, 280, 290, 300, 310, 320, 330, 340]

# Convert Kelvin → Celsius
temps_celsius = [K - 273.15 for K in temps_kelvin]

# Convert Kelvin → Fahrenheit
temps_fahrenheit = [(K - 273.15) * 9/5 + 32 for K in temps_kelvin]

# Print results
for K, C, F in zip(temps_kelvin, temps_celsius, temps_fahrenheit):
    print(f"{K}K = {C:.2f}°C = {F:.2f}°F")
