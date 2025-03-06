import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number!")
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers!")
    return math.log(x, base)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial only defined for non-negative integers!")
    return math.factorial(x)

def main():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")

    while True:
        choice = input("Enter choice(1-11): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"sqrt({num}) = {sqrt(num)}")

        elif choice in ['7', '8', '9']:
            angle = float(input("Enter angle in degrees: "))

            if choice == '7':
                print(f"sin({angle}) = {sin(angle)}")
            elif choice == '8':
                print(f"cos({angle}) = {cos(angle)}")
            elif choice == '9':
                print(f"tan({angle}) = {tan(angle)}")

        elif choice == '10':
            num = float(input("Enter number: "))
            base = float(input("Enter base (default is 10): ") or 10)
            print(f"log({num}, {base}) = {log(num, base)}")

        elif choice == '11':
            num = int(input("Enter number: "))
            print(f"{num}! = {factorial(num)}")

        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()