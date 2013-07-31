import os, sys, shutil, errno

commands=sys.argv[1:]
commandholder=[]

for command in commands:
  if command == commands[0]:
    print command
  elif command > commands[0]:
	commandholder.append(command)
	print commandholder
	shutil.copytree(commands[0],''.join(commandholder))
	commandholder.remove(command)