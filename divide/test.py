import sys, os
from itertools import cycle
outputFolders=cycle(sys.argv[1:])
outputF=[]

outputF.append(outputFolders.next())
print outputF