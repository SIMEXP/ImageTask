import os
import pandas as pd
from flatten import flatten
import platform
def refFinder(category_name):
    cwd = os.getcwd()
    # Adapting the directory paths to the appropriate OS
    if check == 'Windows':
        cat_path = cwd +'\\'+ category_name
    else:
    	cat_path = cwd +'/'+ category_name

    subDirs = [os.path.join(cat_path,dirname) 
              for dirname in os.listdir(cat_path)]
    fPaths = flatten([[os.path.abspath(os.path.join(subDir,filename))
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()])
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()
    shortpathlist = []
    for imName in fPaths.__iter__():
        for ref in references.__iter__():
            refInd = imName.find(ref)
            if refInd != -1:
                longpath, ext = os.path.splitext(imName)
                shortpath = longpath[:longpath.find(ref)]+ext
                shortpathlist.append(shortpath+ext,imName)
    return(shortpathlist,fPaths)
newnames = refFinder('bathroom')