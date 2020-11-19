from random import randint, choice

def checkStreak(result):
    return len(set(result)) == 1 and len(result) >= 6

try:
    number_of_streaks = 0
    coin = ['H', 'T']
    result = []
    flip_qty = int(input('How many times, you wish to flip the coin: '))

    for i in range(flip_qty):
        result.append(choice(coin))
        streak = checkStreak(result[-6:])
        if streak:
            number_of_streaks += 1

    print(f'Chances of streak: {number_of_streaks}. Probability: %{round(number_of_streaks/flip_qty*100, 2)}')
    
except ValueError:
    print('Type a number please!!')