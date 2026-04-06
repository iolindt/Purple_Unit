import sys
from abc import ABC, abstractmethod


class ConversionError(Exception):
    pass


class UnitConverter(ABC):
    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class LengthConverter(UnitConverter):
    factors = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "mile": 1609.34,
        "ft": 0.3048
    }

    def convert(self, value, from_unit, to_unit):
        try:
            base = value * self.factors[from_unit]
            return base / self.factors[to_unit]
        except KeyError:
            raise ConversionError("Invalid length unit")


class WeightConverter(UnitConverter):
    factors = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592,
        "ton": 1000
    }

    def convert(self, value, from_unit, to_unit):
        try:
            base = value * self.factors[from_unit]
            return base / self.factors[to_unit]
        except KeyError:
            raise ConversionError("Invalid weight unit")


class TemperatureConverter(UnitConverter):
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        # convert to Celsius
        if from_unit == "C":
            c = value
        elif from_unit == "F":
            c = (value - 32) * 5 / 9
        elif from_unit == "K":
            c = value - 273.15
        else:
            raise ConversionError("Invalid temperature unit")

        # convert from Celsius
        if to_unit == "C":
            return c
        elif to_unit == "F":
            return c * 9 / 5 + 32
        elif to_unit == "K":
            return c + 273.15
        else:
            raise ConversionError("Invalid temperature unit")


class ConverterFactory:
    converters = {
        "length": LengthConverter(),
        "weight": WeightConverter(),
        "temperature": TemperatureConverter()
    }

    @staticmethod
    def get_converter(category: str) -> UnitConverter:
        if category not in ConverterFactory.converters:
            raise ConversionError("Invalid category")
        return ConverterFactory.converters[category]


class CLI:
    @staticmethod
    def run():
        print("=== Advanced Unit Converter ===")

        while True:
            print("\nCategories: length, weight, temperature")
            category = input("Choose category (or 'exit'): ").lower()

            if category == "exit":
                print("Bye!")
                sys.exit()

            try:
                converter = ConverterFactory.get_converter(category)

                value = float(input("Enter value: "))
                from_unit = input("From unit: ").lower()
                to_unit = input("To unit: ").lower()

                result = converter.convert(value, from_unit, to_unit)
                print(f"Result: {result:.4f}")

            except ValueError:
                print("Invalid number")
            except ConversionError as e:
                print("Error:", e)


if __name__ == "__main__":
    CLI.run()
