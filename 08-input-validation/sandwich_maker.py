#! python3

"""Makes the user a sandwich based on their preferences

JJ Small
"""

import pyinputplus as pyip 

# These are some expensive ingredients
prices = {'wheat': 1, 'white': 1, 'sourdough': 2,
        'chicken': 2, 'turkey': 2, 'ham': 1, 'tofu': 2,
        'cheddar': 1, 'swiss': 1, 'mozzarella': 1,
        'mayo': 1, 'mustard': 1, 'lettuce': 1, 'tomato': 1}

# The sandwich structure
sandwich = {'wheat': 0, 'white': 0, 'sourdough': 0,
        'chicken': 0, 'turkey': 0, 'ham': 0, 'tofu': 0,
        'cheddar': 0, 'swiss': 0, 'mozzarella': 0,
        'mayo': 0, 'mustard': 0, 'lettuce': 0, 'tomato': 0}

        
bread_types = ['wheat', 'white', 'sourdough']
protein_types = ['chicken', 'turkey', 'ham', 'tofu']
cheese_types = ['cheddar', 'swiss', 'mozzarella']

# Now lets make our sandwich!
bread = pyip.inputMenu(bread_types)
sandwich[bread] = 1

protein = pyip.inputMenu(protein_types)
sandwich[protein] = 1

print('Do you want cheese? (yes, no):')
cheese = pyip.inputYesNo()
if cheese == 'yes':
    ctype = pyip.inputMenu(cheese_types)
    sandwich[ctype] = 1

print('Do you want mayo?')
mayo = pyip.inputYesNo()
if mayo == 'yes':
    sandwich['mayo'] = 1

print('Do you want mustard?')
mustard = pyip.inputYesNo()
if mustard == 'yes':
    sandwich['mustard'] = 1

print('Do you want lettuce?')
lettuce = pyip.inputYesNo()
if lettuce == 'yes':
    sandwich['lettuce'] = 1

print('Do you want tomato?')
tomato = pyip.inputYesNo()
if tomato == 'yes':
    sandwich['tomato'] = 1

# How fat are they feeling?
print('How many sandwiches do you want?')
amount = pyip.inputInt(min = 1)

# Give them the total cost of the sandwich
cost = 0
for item, wants in sandwich.items():
    if wants == 1:
        cost += prices[item]

print('Your sandwhich will cost %s$' %(cost * amount))


