import sys
import os
import unittest
import yamf
import subprocess
from yamf import Mock, MockModule, MockArray

programDir=r"D:\users\Karethas_2\Documents\GitHub\divide\divide"
assert os.path.isdir(programDir)
os.chdir(programDir)
output1='D:\users\Karethas_2\Documents\GitHub\divide\divide\output1'
class TestDivision(unittest.TestCase):

  def setUp(self):
    self.argumentsForProgram='divide.py divideTestFolder output1'

  def testGivingArguments(self):
    os.system(self.argumentsForProgram)
    self.assertEquals(os.listdir(output1), ['testFile1.txt', 'testFile2.txt'])

if __name__=='__main__':
  unittest.main()