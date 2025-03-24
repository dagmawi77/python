import numpy as num
from scipy import stats

"""Mean
The mean value is the average value.

To calculate the mean, find the sum of all values, and divide the sum by the number of values:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77"""

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print(num.mean(speed))

"""
Median
The median value is the value in the middle, after you have sorted all the values:

77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

It is important that the numbers are sorted before you can find the median."""

print(num.median(speed ))

"""
Mode
The Mode value is the value that appears the most number of times:

99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

"""

x = stats.mode(speed)

print(x)
