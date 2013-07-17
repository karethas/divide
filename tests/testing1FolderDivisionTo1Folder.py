import sys
import os
import unittest
import yamf
import subprocess
from yamf import Mock, MockModule, MockArray

class TestDivision(unittest.TestCase):

  def setUp(self):
    self.argumentsForProgram=['../codes','divide.py', 'divideTestFolder', 'output1']
  def testGivingArguments(self):
    assert subprocess.call(self.argumentsForProgram)
  def testAcceptance(self):
    self.assertEquals(os.listdir(output1), ['testFile1.txt', 'testFile2.txt'])
if __name__=='__main__':
  unittest.main()