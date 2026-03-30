# Unit Converter
Convert units like kg↔lb and °C↔°F.
import sys

class UnitConverter:
    def __init__(self):
        self.conversion_map = {
            "kg_lb": lambda x: x * 2.20462,
            "lb_kg": lambda x: x / 2.20462,
            "c_f": lambda x: (x * 9/5) + 32,
            "f_c": lambda x: (x - 32) * 5/9
        }

    def convert(self, value, from_unit, to_unit):
        key = f"{from_unit}_{to_unit}"
        if key not in self.conversion_map:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")
        return self.conversion_map[key](value)


def parse_input(user_input):
    try:
        value, units = user_input.strip().split()
        from_unit, to_unit = units.split("->")
        return float(value), from_unit.lower(), to_unit.lower()
    except Exception:
        raise ValueError("Invalid input format. Use: <value> <unit_from->unit_to>")


def main():
    converter = UnitConverter()

    print("Unit Converter CLI")
    print("Examples: 10 kg->lb | 32 f->c | 100 c->f")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter conversion: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            sys.exit()

        try:
            value, from_unit, to_unit = parse_input(user_input)
            result = converter.convert(value, from_unit, to_unit)
            print(f"Result: {round(result, 4)}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
