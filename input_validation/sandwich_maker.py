import pyinputplus as pyip

print('Hi, please order your sandiwch here')

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
cheese = pyip.inputYesNo(prompt='Would you like cheese?')
if cheese == 'yes':
    cheese_type = pyip.inputMenu(['chedar', 'swiss', 'mozzarella'])
extras = pyip.inputYesNo(prompt='Would you like mayo, mustard, lettuce or tomate?')
num_sandwiches = pyip.inputNum(prompt='How many sandwiches you want?', min=1)

print(bread, protein, cheese, cheese_type, extras)