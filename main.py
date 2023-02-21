# Fibonacci Series Generator
import time


def fibonacci(number):
    n1 = 0
    n2 = 1
    count = 0
    if number <= 0:
        print("Please enter a number greater than zero! Negative Numbers cannot be a input for length of the sequence")
    if number == 1:
        print(n1)
    elif number == 2:
        print(n2)
    elif number > 2:
        while count < number:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


def run_program():
    sequence_generator_is_running = True
    while sequence_generator_is_running:
        print("Welcome to the Fibonacci sequence generator ")
        user_input = input("How many numbers do you need in the sequence?: ").lower()
        if user_input == "exit":
            print("Closing the sequence generator")
            time.sleep(1)
            sequence_generator_is_running = False
        elif user_input.isnumeric():
            fibonacci(int(user_input))


run_program()
