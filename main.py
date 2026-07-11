from formatter import header
from length import meters_to_kilometers
from weight import kilograms_to_grams
from temperature import fahrenheit_to_celsius
from history import add, show

header()

km = meters_to_kilometers(1500)
print(f"1500 m = {km:.2f} km")
add("1500 m -> 1.50 km")

grams = kilograms_to_grams(5)
print(f"5 kg = {grams} g")
add("5 kg -> 5000 g")

celsius = fahrenheit_to_celsius(32)
print(f"32°F = {celsius:.0f}°C")
add("32°F -> 0°C")

show()
