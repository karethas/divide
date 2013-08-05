import os, sys, shutil, errno

commands=sys.argv[1:]
commandholder=[]
DirectoryContent=os.listdir(commands[0])

for command in commands:
  if command == commands[0]:
    print "Division in progress."
  elif command > commands[0]:
	commandholder.append(command)
	os.mkdir(''.join(commandholder))
	print os.path.getsize(commandholder)/len(commandholder)