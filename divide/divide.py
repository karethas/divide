import os, sys, shutil, errno

sourceFolder=sys.argv[1]

sourceFolderContent=os.listdir(sourceFolder)

def createOutputFolders():
  outputFolders=sys.argv[2:]
  for outputFolder in outputFolders:
    os.mkdir(''.join(outputFolder)) 

  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceFolderContent:
    contentSize+=os.path.getsize(os.path.join(sourceFolder,content))
  print contentSize
  return contentSize
  
def getOutputFolderContentSize():
  outputSize=0
  for content in outputFolder:
	outputSize+=os.path.getsize(os.path.join(outputFolder,content))
  return outputSize

def divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, getOutputFolderContentSize):
  sourceFolderContentSize=getSourceFolderContentSize()
  outputFolderContentSize=getOutputFolderContentSize()
  for content in sourceFolderContent:
        shutil.copy(os.path.join(sourceFolder,content),os.path.join(outputFolders, content)


getSourceFolderContentSize()
createOutputFolders()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, getOutputFolderContentSize)