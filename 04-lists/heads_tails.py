# JJ Small - 01/01/2020
# 
# Write a program to find out how often a streak of 6 heads of 6 tails will occur in a randomly
# generated list of heads and tails.
#
# Note: Heads = 0 and Tails = 1
import random
import time

# This function will generate a list of 100 heads/tails flips
def make_list():
    flips = [random.randint(0,1) for i in range(100)]
    return flips

# Returns true if the passed in list contains at least one streak of 6 heads or tails
def has_streak(flip_list):
    streak_count = 0
    l = len(flip_list)

    for i in range(0, l - 1):
        if streak_count == 5:
            return True
        else:
            if flip_list[i] == flip_list[i+1]:
                streak_count += 1
            else:
                streak_count = 0

    return False

# Iterate 10000 times to determine how many successful 6 in a rows we get
start_time = time.time()

number_of_streaks = 0
for n in range(10000):
    flips = make_list()
    if has_streak(flips):
        number_of_streaks += 1

print(number_of_streaks)
print('Chance of streaks: %s%%' % (number_of_streaks / 100))
print("--- %s seconds ---" % (time.time() - start_time))