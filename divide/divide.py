import os, sys, shutil, errno

def dividingFolder():
  os.mkdir(sys.argv)
  


def main():
  if sys.argv:
    print 'usage: ./divide.py sourcefolder outputfolder'
    sys.exit(1)

if __name__ == '__main__':
  main()