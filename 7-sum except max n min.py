'''Sum all the numbers of a given array ( cq. list ), 
except the highest and the lowest element ( by value, not by index! ). 
You cannot use the if statement.
{ 6, 2, 1, 8, 10 } => 16 / { 1, 1, 11, 2, 3 } => 5'''

a = { 1, 1, 11, 2, 3 }

a.remove(max(a))
a.remove(min(a))

print(a)

print(sum(a))

# THE END