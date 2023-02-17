import os
import shutil 

baseDir = os.getcwd()
fileName = 'story2.txt'


with os.scandir(baseDir) as dirs:
    for dir in dirs:
        if os.path.isdir(dir.name):
            parentdir = baseDir + "/" + dir.name 
        with os.scandir(parentdir) as parentdirs:
            for pdir in parentdirs:
                if os.path.isdir(pdir):
                    filePath = os.path.join(parentdir + "/" + pdir.name, fileName)
                    # file2path = parentdir + '/'+pdir.name+fname
                    # if os.path.exists(file2path):
                    #     os.remove(file2path)
                    if not os.path.exists(filePath):
                        with open(filePath, 'w') as nothing: 
                            pass
                        