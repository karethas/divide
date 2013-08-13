import os, sys, shutil, errno

sourceFolder=sys.argv[1]
outputFolders=sys.argv[2:]
sourceFolderContent=os.listdir(sourceFolder)

def createOutputFolders(outputFolders):
  for outputFolder in outputFolders:
    os.mkdir(''.join(outputFolder)) 

  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceFolderContent:
    contentSize+=os.path.getsize(os.path.join) IMPLEMENT
  return contentSize
  
def getOutputFolderContentSize():
  outputSize=0
	outputSize+=os.path.getsize(os.path.join) IMPLEMENT	  
  return outputSize

def divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, getOutputFolderContentSize):
  fileIterator=0
  folderIterator=0
  sourceFolderContentSize=getSourceFolderContentSize()
  outputFolderContentSize=getOutputFolderContentSize()
  while folderIterator<len(outputFolders):
        shutil.copy(sourceFolder+'/'+sourceFolderContent[fileIterator],''.join(outputFolders[folderIterator]))
	fileIterator+=1
	folderIterator+=1
	print outputFolderContentSize
  if outputFolderContentSize>=sourceFolderContentSize/len(outputFolders):
	  print 'life is perfect'  
	 

createOutputFolders(outputFolders)
getSourceFolderContentSize()
getOutputFolderContentSize()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, getOutputFolderContentSize)