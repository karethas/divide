import sys
import os
import unittest
import yamf
import subprocess
from yamf import Mock, MockModule, MockArray
argumentsForProgram=['../codes','divide.py', 'divideTestFolder', 'output1']
assert subprocess.call(argumentsForProgram)
assertEquals (os.listdir(output1), ['testFile1.txt', 'testFile2.txt'])