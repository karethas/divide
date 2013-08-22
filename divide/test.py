import os, sys, shutil, errno

sourceFolder=sys.argv[1]
outputFolders=sys.argv[2:]
sourceFolderContent=os.listdir(sourceFolder)

def createOutputFolders():
  for outputFolder in outputFolders:
    os.mkdir(outputFolder) 
  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceFolderContent:
    contentSize+=os.path.getsize(os.path.join(sourceFolder,content))
  return contentSize

def getOutputFolderSize(outputFolders):
  contentSize=0
  for content in outputFolders[0]:
    contentSize+=os.path.getsize(os.path.join(outputFolders[0],content))
  return contentSize

def folderSwapper(outputFolders,usedFolders):
  usedFolders.append(outputFolders[0])
  outputFolders.pop(0)
  print usedFolders
  if outputFolders == []:
	outputFolders.append(usedFolders[0])

  
def divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, getOutputFolderSize, folderSwapper):
  usedFolders=[]
  sourceFolderContentSize=getSourceFolderContentSize()
  limitToOutputFolderContentSize=sourceFolderContentSize/len(outputFolders)
  swapFolder=folderSwapper(outputFolders, usedFolders)
  outputFolderSize=getOutputFolderSize(outputFolders)
  print limitToOutputFolderContentSize
  for content in sourceFolderContent:
    shutil.copy(os.path.join(sourceFolder,content),os.path.join(outputFolders[0], content))
    outputFolderSize
    print outputFolderSize
    if outputFolderSize>=limitToOutputFolderContentSize:
      swapFolder
	

createOutputFolders()
getSourceFolderContentSize()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, getOutputFolderSize, folderSwapper)