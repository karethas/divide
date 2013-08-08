import os, sys, shutil, errno

commands=sys.argv[1:]
outputFolders=sys.argv[:1]
folderName=[]
directoryContent=os.listdir(commands[0])
contentSize=0

def getSourceFolderSize():
  for content in directoryContent:
    contentSize+=os.path.getsize(commands[0]+'/'+content)

def createOutputFolders():
	os.mkdir(''.join(outputFolders))

def divideFilesToFolders():
  for command in commands:
    folderName.append(command)  
    fileIterator=0
    folderIterator=0
    if os.path.getsize(''.join(folderName[folderIterator]))<os.path.getsize(commands[0])/len(lengthOfArgumentsAfterArg0):
      shutil.copy(commands[0]+'/'+directoryContent[fileIterator],''.join(folderName[folderIterator]))
      fileIterator+=1
    else:
	  folderIterator+=1