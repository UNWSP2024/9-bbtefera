# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def write_random_numbers():
    print('In the write_random_numbers function')
    try:
        count = int(input("Enter the number of random numbers to generate (up to 1000): "))
        if count < 1 or count > 1000:
            print("Error: Number must be between 1 and 1000.")
            return
        with open('random_numbers.txt', 'w') as file:
            for _ in range(count):
                file.write(str(random.randint(1, 500)) + '\n')
        print(f"{count} random numbers have been written to random_numbers.txt")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == '__main__':
    write_random_numbers()
