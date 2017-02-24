import re

s = '"ddd"xxxx"eeeee"'
a = re.findall('"(.*?)"', s)
print a
