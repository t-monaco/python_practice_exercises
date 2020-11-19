from random import randint
import sys

start_range = int(sys.argv[1])
end_range = int(sys.argv[2])

number = randint(start_range, end_range)

while True:
    try:
        user_number = int(input(f'Type a number from {start_range} to {end_range}\n'))
        if number == user_number:
            print('Well done!! You are a genious!')
            break
        else:
            print('Keep trying!!')
    except ValueError:
        print('Please enter a number!! IDIOT')
        continue