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
  print limitToOutputFolderContentSize
  while not len(outputFolders)==0:
    if os.path.getsize(outputFolders[0])<limitToOutputFolderContentSize:
      for content in sourceFolderContent:
        shutil.copy(os.path.join(sourceFolder,content),os.path.join(outputFolders[0], content))
    """if os.path.getsize(outputFolders[0])>=limitToOutputFolderContentSize:
      outputFolders.pop(0)
      print outputFolders"""
	
createOutputFolders()
getSourceFolderContentSize()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize)