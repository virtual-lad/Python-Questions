'''You get an array of numbers, and return the sum of all of the positive ones.
Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the if statement.'''

a = [1, -4, 7, 12]

result = sum(max(0,i)for i in a)

print(result)


# THE END