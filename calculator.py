try:
    number_one = float(input("Please input your first number: "))
    number_two = float(input("\nPlease input your second number: "))
    op = input("\nPlease enter your operator: ")

    if op == "+":
        print(number_one + number_two)
    elif op == "-":
        print(number_one - number_one)
    elif op == "*" or op == "x":
        print(number_one * number_two)
    elif op == "/":
        print(number_one / number_two)
    elif op == "//":
        print(number_one // number_two)
    elif op == "^" or op == "**":
        print(number_one ** number_two)
    else: 
        print("An error has occured, please check that you have put in valid arguements")

except:
    print("\n\nOperation cancelled\n")