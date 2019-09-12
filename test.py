import sys
import fnmatch
import os
 
rootPath = 'c:\\Users\\boome\\documents\\'
pattern = '*.pptx'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
print('end of the line')