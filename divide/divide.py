import os, sys, shutil, errno

commands=sys.argv[1:]
commandHolder=[]
folderName=[]
directoryContent=os.listdir(commands[0])
contentSize=0
lengthOfArgumentsAfterArg0=[]

for content in directoryContent:
    contentSize+=os.path.getsize(commands[0]+'/'+content)


for command in commands:
  if command == commands[0]:
    print "Division in progress."
  elif command > commands[0]:
	commandHolder.append(command)
	os.mkdir(''.join(commandHolder))
	lengthOfArgumentsAfterArg0.append(command)
	commandHolder.remove(command)


for command in commands:
  folderName.append(command)  
  fileIterator=0
  folderIterator=0
  if os.path.getsize(''.join(folderName[folderIterator]))<os.path.getsize(commands[0])/len(lengthOfArgumentsAfterArg0):
    shutil.copy(commands[0]+'/'+directoryContent[fileIterator],''.join(folderName[folderIterator]))
    fileIterator+=1
  else:
	folderIterator+=1
	
print contentSize/len(lengthOfArgumentsAfterArg0)

print directoryContent
print len(lengthOfArgumentsAfterArg0)
print os.path.getsize(commands[0]+'/')

