class Calculator:
    def add(a, b):
        return a+b
    def subtract(a, b):
        return a-b
    def multiply(a, b):
        return a*b
    def divide(a, b):
        try:
            return a//b
        except:
            return "Error: Division by zero is not allowed"
def main():
    a,b=map(int,input().split())
    print(f"Addition of ({a}+{b}): {Calculator.add(a,b)}")
    print(f"Subtraction of ({a}-{b}): {Calculator.subtract(a,b)}")
    print(f"Multiplying of ({a}*{b}): {Calculator.multiply(a,b)}")
    print(f"Division of ({a}//{b}): {Calculator.divide(a,b)}")
main()
