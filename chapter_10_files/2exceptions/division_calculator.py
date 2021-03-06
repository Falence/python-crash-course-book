print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    except ValueError:
        print("Addition cannot be performed on text!")
    else:
        print(answer)