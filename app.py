welcome_text = "Welcome! This is my first calculator!"

print(f"{welcome_text}\n")

total = 0

number1 = int(input("Enter the first number that you want to calculate with: "))

select_mode = input("Type\nA to Addition\nS to Subtrace\nM to Multiply\nD to Division\n\n")

number2 = int(input("Enter the second number that you want to calculate with: "))

if select_mode == "A":
    total = number1 + number2
    print(total)

elif select_mode == "S":
    total = number1 - number2
    print(total)

elif select_mode == "M":
    total = number1 * number2
    print(total)

elif select_mode == "D":
    total = number1 / number2
    print(total)

add_more = input("Do you want to add mor numbers?\n")

if add_more == "Yes":
    number3 = int(input("Enter the third number:\n"))

    select_mode = (input("Type\nA to Addition\nS to Subtrace\nM to Multiply\nD to Division\n\n"))

    if select_mode == "A":
        total2 = total + number3
        print(total2)

    if select_mode == "S":
        total2 = total - number3
        print(total2)

    elif select_mode == "M":
        total2 = total * number3
        print(total2)

    elif select_mode == "D":
        total2 = total / number3
        print(total2)