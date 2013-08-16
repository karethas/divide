import os, sys, shutil, errno

sourceFolder=sys.argv[1]
outputFolders=sys.argv[2:]
sourceFolderContent=os.listdir(sourceFolder)

def createOutputFolders():
  for outputFolder in outputFolders:
    os.mkdir(''.join(outputFolder)) 
  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceFolderContent:
    contentSize+=os.path.getsize(os.path.join(sourceFolder,content))
  return contentSize

def divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize):
  sourceFolderContentSize=getSourceFolderContentSize()
  limitToOutputFolderContentSize=sourceFolderContentSize/len(outputFolders)
  sizeOfOutputFolder=0
  print limitToOutputFolderContentSize
  for content in sourceFolderContent:
    shutil.copy(os.path.join(sourceFolder,content),os.path.join(outputFolders[0], content))
    sizeOfOutputFolder+=os.path.getsize(os.path.join(outputFolders[0],content)) 
    if sizeOfOutputFolder>=limitToOutputFolderContentSize:
	  outputFolders.append(outputFolders[0])
	  outputFolders.pop(0)
	  
"""^^^Is moving the existing folder from beginning to end and then removing the one at the beginning.
This was a necessary modification to avoid a failure with more files and different sizes"""

	
createOutputFolders()
getSourceFolderContentSize()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize)