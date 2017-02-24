import re

a = [1, 2]
b = [2, 3, 4]
c = [5, 6]

print list(set(a).union(set(b)).union(set(c)))
