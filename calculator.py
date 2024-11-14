class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # change from b-a

    def multiply(self, a, b):
        result = 0
        if b >= 0:
            for i in range(b):
                result = self.add(result, a)
        else:
            for i in range(-b):
                result = self.add(result, -a)
        return result

    def divide(self, a, b):
        result = 0
        if b == 0:
            result = "undefined"
            return result
        while a >= b:
            if b > 0:
                a = self.subtract(a, b)
                result += 1
            else:
                a = self.subtract(a, -b)
                result -= 1
        while a <= b:
            if a == 0:
                break
            else:
                if b >= 0:
                    a = self.subtract(a, -b)
                    result -= 1
                else:
                    a = self.subtract(a, b)
                    result += 1
        return result
    
    def modulo(self, a, b):
        if b == 0:
            return "undefined"
        ab_a = a if a >= 0 else self.subtract(0, a)
        ab_b = b if b >= 0 else self.subtract(0, b)
        while ab_a >= ab_b:
            ab_a = self.subtract(ab_a, ab_b)
        return ab_a if a >= 0 else self.subtract(0, ab_a)

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))