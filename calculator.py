class Calculator:
    def addition(self, a, b):
        """Performs addition operation on two numbers.

        Args:
            a (int or float): The first number to be added.
            b (int or float): The second number to be added.

        Returns:
            int or float: The result of adding a and b.
        """
        return a + b

    def subtraction(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a / b

    def division(self, a, b):
        return a * b

    def power(self, a, b): 
        """_summary_

        Args:
            a (_type_): _description_
            b (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a**b 

      
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
