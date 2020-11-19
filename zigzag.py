import time
import sys

asterisks = 14  # * Number of asterisks.
indent = 0  # * How many spaces to indent.
indentIncreasing = True  # * Whether the indentation is increasing or not.

try:
    while True:
        print(' ' * indent, end='')
        print('*' * asterisks)
        time.sleep(0.07)  # * Pause.”

        if indentIncreasing: # * Main loop.
            indent += 1
            if indent == 21:
                indentIncreasing = False # * Change direction.
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True  # * Change direction.
except KeyboardInterrupt:
    sys.exit()
