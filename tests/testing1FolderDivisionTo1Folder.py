import sys
import os
import unittest
import yamf
import subprocess
from yamf import Mock, MockModule, MockArray

programDir=r"D:\users\Karethas_2\Documents\GitHub\divide\divide"
assert os.path.isdir(programDir)
os.chdir(programDir)
output1='..\divide\output1'
output2='..\divide\output2'
output3='..\divide\output3'

class TestDivision(unittest.TestCase):

  def setUp(self):
    self.argumentsForProgram='divide.py divideTestFolder output1 output2 output3'

  def testGivingArguments(self):
    os.system(self.argumentsForProgram)
    self.assertEquals(os.listdir(output1), ['testFile1.txt'])
    self.assertEquals(os.listdir(output2), ['testFile2.txt'])
    self.assertEquals(os.listdir(output3), ['testFile3.txt'])

	
	
if __name__=='__main__':
  unittest.main()