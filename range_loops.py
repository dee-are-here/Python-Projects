#

# for number in range(1, 11):
# print(number)
# for the numbers in the range, the first number is the starting point
# and the second number is the stopping point.
# The stopping point is not included in the range.
# So in this case, it will print the numbers 1 through 10.

# for number in range(1, 11, 3):
#  print(number)
# The third number in the range is the step.
# So in this case, it will print the numbers 1, 4, 7, and 10.

total = 0
for number in range(1, 101):
    total += number
print(total)

# This will print the sum of the numbers from 1 to 100.
