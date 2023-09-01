class FractionError(Exception):
    """Base class for fraction-related exceptions."""
    pass


class InvalidFractionError(FractionError):
    """The exception raised when the fraction format is invalid."""
    def __init__(self, fraction_str):
        super().__init__(f"Неверный формат дроби: {fraction_str}")


class DivisionByZeroError(FractionError):
    """The exception that is thrown when an attempt
    is made to divide by zero."""
    def __init__(self):
        super().__init__("Деление на ноль невозможно")


class FractionCalculator:
    def __init__(self):
        self.fraction1 = None
        self.fraction2 = None

    def find_gcd(self, a, b):
        """Finds the greatest common divisor of two numbers."""
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_fraction(self, numerator, denominator):
        """Simplifies a fraction to its smallest manifest form."""
        common_divisor = self.find_gcd(numerator, denominator)
        return numerator // common_divisor, denominator // common_divisor

    def parse_fraction(self, fraction_str):
        """Parses a string containing a fraction and returns
        the numerator and denominator."""
        parts = fraction_str.split("/")
        if len(parts) != 2:
            raise InvalidFractionError(fraction_str)
        numerator, denominator = map(int, parts)
        if denominator == 0:
            raise DivisionByZeroError()
        return numerator, denominator

    def input_fractions(self):
        """Gets user input for two fractions."""
        try:
            self.fraction1 = input("Введите первую дробь в формате a/b: ")
            self.fraction2 = input("Введите вторую дробь в формате a/b: ")

            self.parse_fraction(self.fraction1)
            self.parse_fraction(self.fraction2)
        except (InvalidFractionError, DivisionByZeroError) as e:
            raise FractionError(str(e)) from None

    def calculate(self):
        """Performs calculations for two fractions and
        displays the results on the screen."""
        try:
            self.input_fractions()

            num1, den1 = self.parse_fraction(self.fraction1)
            num2, den2 = self.parse_fraction(self.fraction2)

            common_denominator = den1 * den2
            new_num1 = num1 * den2
            new_num2 = num2 * den1

            sum_numerators = new_num1 + new_num2
            sum_result = self.simplify_fraction(sum_numerators,
                                                common_denominator)

            product_numerator = num1 * num2
            product_denominator = den1 * den2
            product_result = self.simplify_fraction(product_numerator,
                                                    product_denominator)

            return (f"Сумма дробей: {sum_result[0]}/{sum_result[1]}, "
                    f"Произведение дробей: "
                    f"{product_result[0]}/{product_result[1]}")

        except FractionError as e:
            return str(e)


calculator = FractionCalculator()
result = calculator.calculate()
print(result)
