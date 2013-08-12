import os, sys, shutil, errno

sourceFolder=sys.argv[1]
outputFolders=sys.argv[2:]
sourceContent=os.listdir(sourceFolder)

def createOutputFolders(outputFolders):
  rotator=0
  yksinimikerrallaan=[]
  while len(outputFolders)>rotator:
    yksinimikerrallaan.append(outputFolders[rotator])
    os.mkdir(''.join(yksinimikerrallaan)) 
    yksinimikerrallaan.remove(outputFolders[rotator])
    rotator+=1
  return 
createOutputFolders(outputFolders)
  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceContent:
    contentSize+=os.path.getsize(sourceFolder+'/'+content)
  return contentSize
  
def getOutputFolderContentSize():
  outputSize=0
  outputContent=os.listdir(outputFolders)
  container=[]
  for content in outputFolders:
        container.append(content)
	outputSize+=os.path.getsize(container+'/'+content)
	container.remove(content)	  
  return outputSize

def divideFilesToFolders(sourceFolder, outputFolders, sourceContent, getSourceFolderContentSize, getOutputFolderContentSize):
  fileIterator=0
  folderIterator=0
  sourceFolderContentSize=getSourceFolderContentSize()
  outputFolderContentSize=getOutputFolderContentSize()
  while folderIterator<len(outputFolders):
        shutil.copy(sourceFolder+'/'+sourceContent[fileIterator],''.join(outputFolders[folderIterator]))
	fileIterator+=1
	folderIterator+=1
	print outputFolderContentSize
  if outputFolderContentSize>=sourceFolderContentSize/len(outputFolders):
	  print 'life is perfect'  

divideFilesToFolders(sourceFolder, outputFolders, sourceContent, getSourceFolderContentSize, getOutputFolderContentSize)