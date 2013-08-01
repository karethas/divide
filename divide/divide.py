import os, sys, shutil, errno

commands=sys.argv[1:]
commandholder=[]
directoryContent=os.listdir(commands[0])

for command in commands:
  if command == commands[0]:
    print command
  elif command > commands[0]:
	commandholder.append(command)
	os.mkdir(''.join(commandholder))
	
	commandholder.remove(command)