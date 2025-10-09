import math
som = 1
getal1 = 1
getal2 = 1

while True:
    def num1Input():
        while True:
            temp = input("Insert the first number: ")
            try:
                return float(temp)
            except ValueError:
                print("Please only type numbers")
    def num2Input():
        while True:
            temp = input("Insert the second number: ")
            try:
                return float(temp)
            except ValueError:
                print("Please type only numbers")

    def typeInput():
        while True:
            temp = input("Select type(+, -, *, /, %, ^, abs, !, avg): ")
            if temp in ["+", "-", "*", "/", "%", "^", "abs", "!", "avg"]:
                return temp
            print("Unknown parameter try again")

    getal1 = num1Input()
    getal2 = num2Input()
    operator = typeInput()

    if operator == "+":
        som = getal1 + getal2
        print(f"{getal1} + {getal2} = {som}")
    elif operator == "-":
        som = getal1 - getal2
        print(f"{getal1} - {getal2} = {som}")
    elif operator == "*":
        som = getal1 * getal2
        print(f"{getal1} * {getal2} = {som}")
    elif operator == "/":
        som = getal1 / getal2
        print(f"{getal1} / {getal2} = {som}")
    elif operator == "%":
        som = getal1 % getal2
        print(f"{getal1} % {getal2} = {som}")
    elif operator == "^":
        som = getal1 ** getal2
        print(f"{getal1} ^ {getal2} = {som}")
    elif operator == "abs":
        som = abs(getal1)
        print(f"|{getal1}| = {som}")
    elif operator == "!":
        som = math.factorial(int(getal1))
        print(f"{int(getal1)}! = {som}")
    elif operator == "avg":
        som = (getal1 + getal2) / 2
        print(f"The average of {getal1} and {getal2} is {som}")
    else:
        print("There has been an error. Please try again. If issue persists please create an issue through GitHub.")