import os, sys, shutil, errno

commands=sys.argv[1:]
commandholder=[]
directoryContent=os.listdir(commands[0])
lengthOfArgumentsAfterArg0=[]

for command in commands:
  if command == commands[0]:
    print "Division in progress."
  elif command > commands[0]:
	commandholder.append(command)
	os.mkdir(''.join(commandholder))
	lengthOfArgumentsAfterArg0.append(command)
	commandholder.remove(command)

print directoryContent
print len(lengthOfArgumentsAfterArg0)
print os.path.getsize(commands[0])
print os.path.getsize(commands[0])/len(lengthOfArgumentsAfterArg0)