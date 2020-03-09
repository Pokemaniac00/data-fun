#!/bin/env python
import sys
import os
from shutil import move

def isValid(filename):
    file = open(filename, "r")
    if "Keyword" in file.read():
        file.close()
        return False
    else:
        file.close()
        return True
    
def main():
    print('Sorting files...')
    argList = sys.argv
    argList.remove("checkData.py")
    fileList = [s.replace("data/", "") for s in argList]

    for i in range(0, len(fileList)):
        if(isValid(argList[i])):
            move(argList[i], "valid/" + fileList[i])
        else:
            move(argList[i], "invalid/" + fileList[i])
    
    print('Sorted.')

main()