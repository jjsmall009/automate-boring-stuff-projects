#! python3

import re

# Create the date regex

date_pattern = re.compile(r'''
    (0[1-9]|[12][0-9]|3[01])\/ # Day from 00-31
    (0[1-9]|1[0-2])\/          # Month from 00-12
    ([1-2]\d{3})               # Year from 1000-2999
    ''', re.VERBOSE)

matches = date_pattern.findall('30/02/2020 15/12/1645 01/01/1000 08/06/2999 34/15/768')

# Setup the things we need
valid_dates = []
invalid_dates = []
thirty_days = ['04', '06', '09', '11']
thirty1_days = ['01', '03', '05', '07', '08', '10', '12']

for date in matches:
    valid = True
    day = date[0]
    month = date[1]
    year = date[2]

    # First determine if it's valid by checking the leap years
    if month == '02':
        year = int(year)
        if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
            if day > '29':
                valid = False
        else:
            if day > '28':
                valid = False

    # Secondly we check if day is within the bounds for that month
    if (month in thirty_days and day > '30') or (month in thirty1_days and day > '31'):
        valid = False
    
    # Lastly we add the date into its proper list
    if valid:
        valid_dates.append('/'.join(date))
    else:
        invalid_dates.append('/'.join(date))

# Display the valid dates and also the invalid ones
print('Valid dates are:')
print('================')
for d in valid_dates:
    print(d)

print('\nInvalid dates are:')
print('==================')
for d in invalid_dates:
    print(d)