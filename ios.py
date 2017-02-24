import re




s391 = open('391.txt')
list391 = re.findall('"(.*?)"', s391.read())

s385 = open('385.txt')
list385 = re.findall('"(.*?)"', s385.read())


android = list(set(list391)
               .union(set(list385))
               .union(set(list391))

               )

print list(set(android).union(set(android)))
