import os, sys, shutil, errno, distutils.core
sourceFolder=sys.argv[1]
outputFolders=sys.argv[2:]
sourceFolderContent=os.listdir(sourceFolder)

def createOutputFolders():
  for outputFolder in outputFolders:
    if os.path.exists(outputFolder)!=True:
      os.mkdir(outputFolder)
  
def getSourceFolderContentSize():
  contentSize=0
  for content in sourceFolderContent:
    contentSize+=os.path.getsize(os.path.join(sourceFolder,content))
  return contentSize

def folderSwapper(outputFolders,usedFolders):
  usedFolders.append(outputFolders[0])
  outputFolders.pop(0)
  if outputFolders == []:
	outputFolders.append(usedFolders[0])

  
def divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, folderSwapper):
  contentSize=0
  usedFolderContentSize=0
  usedFolders=[]
  limitToOutputFolderContentSize=getSourceFolderContentSize()/len(outputFolders)
  print limitToOutputFolderContentSize
  for content in sourceFolderContent:
    try:
      shutil.copy(os.path.join(sourceFolder,content),os.path.join(outputFolders[0], content))
      contentSize+=os.path.getsize(os.path.join(outputFolders[0],content))
      if contentSize>=limitToOutputFolderContentSize:
	    folderSwapper(outputFolders,usedFolders)
    except IOError:  distutils.dir_util.copy_tree(os.path.join(sourceFolder,content),outputFolders[0])

createOutputFolders()
getSourceFolderContentSize()
divideFilesToFolders(sourceFolder, outputFolders, sourceFolderContent, getSourceFolderContentSize, folderSwapper)