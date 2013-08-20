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

def divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize):
  sourceFolderContentSize=getSourceFolderContentSize()
  limitToOutputFolderContentSize=sourceFolderContentSize/len(outputFolders)
  sizeOfOutputFolder=0
  usedFolders=[]
  print limitToOutputFolderContentSize
  for content in sourceFolderContent:
    shutil.copy(os.path.join(sourceFolder,content),os.path.join(outputFolders[outputFolderChanger], content))
    sizeOfOutputFolder+=os.path.getsize(os.path.join(outputFolders[outputFolderChanger],content)) 
    if sizeOfOutputFolder>=limitToOutputFolderContentSize:
      usedFolders.append(outputFolders[])
	if folder in usedFolders:
	  print "temporary no message until the utility for this is corrected."
	if outputFolders == outputfolders[-1]:
	  sizeList=[]
	  os.path.getsize(usedFolders[0])
	  

createOutputFolders()
getSourceFolderContentSize()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize)