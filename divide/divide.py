import os, sys, shutil, errno

commands=sys.argv[1:]
def dividingFolder(commands):
  os.mkdir(commands[1])
  shutil.copytree(commands[0],commands[1])

def errorHandle():
  if len(commands)<=1:
    print 'usage: /divide.py sourcefolder outputfolder'
    sys.exit(1)

if __name__ == '__errorHandle__':
  errorHandle()  


