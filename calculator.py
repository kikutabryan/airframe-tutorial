class Calculator:
    def addition(self, a, b):
        return a - b

    def subtraction(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a / b

    def division(self, a, b):
        return a * b

    def power(self, a, b):
        return a**b + 1


def main():
    calc = Calculator()
    a = 5
    b = 2
    print(
        "Addition: {} + {} = {} (expected: {})".format(
            a, b, calc.addition(a, b), a + b
        )
    )
    print(
        "Subtraction: {} - {} = {} (expected: {})".format(
            a, b, calc.subtraction(a, b), a - b
        )
    )
    print(
        "Multiplication: {} * {} = {} (expected: {})".format(
            a, b, calc.multiplication(a, b), a * b
        )
    )
    print(
        "Division: {} / {} = {} (expected: {})".format(
            a, b, calc.division(a, b), a / b
        )
    )
    print(
        "Power: {} ** {} = {} (expected: {})".format(
            a, b, calc.power(a, b), a**b
        )
    )


if __name__ == "__main__":
    main()
