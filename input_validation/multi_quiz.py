import pyinputplus as pyip
import time
import random

number_of_questions = 10
correct_answers = 0

for question_num in range(number_of_questions):
    # pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'#{question_num + 1}: {num1} x {num2} = '

    try:
        # Right answers are handle by allowRegex
        # Wrong answers are handle by blockRegex
        pyip.inputStr(prompt,
                      allowRegexes=[f'^{(num1 * num2)}$'],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8,
                      limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block is run when no excaptions were raised in the try block
        print('Correct!')
        correct_answers += 1
    time.sleep(1)  # Brief pause to let the user see the result
print(f'Score: {correct_answers}/{number_of_questions}')
