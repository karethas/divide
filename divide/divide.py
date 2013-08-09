import os, sys, shutil, errno

sourceFolder=sys.argv[1]
outputFolders=sys.argv[2:]
sourceContent=os.listdir(sourceFolder)
outputContent=os.listdir(outputFolders)

print ''.join(outputFolders)
def createOutputFolders(outputFolders):
  rotator=0
  yksinimikerrallaan=[]
  while len(outputFolders)>rotator:
    yksinimikerrallaan.append(outputFolders[rotator])
    os.mkdir(''.join(yksinimikerrallaan)) 
    yksinimikerrallaan.remove(outputFolders[rotator])
    rotator+=1
  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceContent:
    contentSize+=os.path.getsize(sourceFolder+'/'+content)
  return contentSize

def getOutputFolderContentSize():
  contentSize=0
  for content in outputContent:
    contentSize+=os.path.getsize(outputContent+'/'+content)
  
def divideFilesToFolders(sourceFolder, getSourceFolderContentSize):
  fileIterator=0
  folderIterator=0
  sourceFolderContentSize=getSourceFolderContentSize()
  while os.path.getsize(''.join(outputFolders[folderIterator]))<sourceFolderContentSize/len(outputFolders):
    shutil.copy(sourceFolder+'/'+sourceContent[fileIterator],''.join(outputFolders[folderIterator]))
    fileIterator+=1
  else:
	folderIterator+=1
	
createOutputFolders(outputFolders)
getSourceFolderContentSize()
divideFilesToFolders(sourceFolder, getSourceFolderContentSize)