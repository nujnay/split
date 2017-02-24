import os
import re

listThis = []

print os.getcwd()

dir = os.getcwd()
foldThis = os.walk(dir)
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print ';;;;;;;'
        print name._formatter_field_name_split()
print foldThis

