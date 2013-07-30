import os, sys, shutil, errno

commands=sys.argv[1:]
shutil.copytree(commands[0],commands[1])
