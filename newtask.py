# def is_even(number):
#     return (number // 2) * 2 == number

# def main():
#     number = int(input("Enter a number: "))
#     if is_even(number):
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")

# main()

def swap_numbers_list(a, b):
    numbers = [a, b]
    numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers[0], numbers[1]

def main():
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    print(f"Before swapping: {a}{b}")
    a, b = swap_numbers_list(a, b)
    print(f"After swapping:{a}{b}")


main()

