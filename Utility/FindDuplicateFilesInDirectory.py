#!/usr/bin/python

'''
A python script to get duplicate files by comparing hashes of files in all sub-directories of a directory
'''

import hashlib
import os
import json

All_Files_Hash ={}

def Get_MD5_File_Hash(FilePath):
    hash_md5 = hashlib.md5()
    try:
        with open(FilePath,"rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
    except Exception as ex:
        print(ex)
        return "ss"
    return hash_md5.hexdigest()

def Generate_Hashes_Of_Files_And_Search_Duplicates(rootDirPath):
    for dir, subDir, files in os.walk(rootDirPath):
        for file in files:
            filePath = os.path.join(dir,file)
            fileHash = Get_MD5_File_Hash(filePath)
            if(fileHash=="ss"):
                continue
            if fileHash in All_Files_Hash:
                All_Files_Hash[fileHash].append(filePath)
                print(f"Duplicate: {All_Files_Hash[fileHash]}")
            else:
                temp=[]
                temp.append(filePath)
                All_Files_Hash[fileHash]=temp

#Needs some work
def Save_Data_To_JSON_File():
    with open("DuplicateFiles.json","w+") as f:
        json.dump(All_Files_Hash,f,indent=4)

if __name__ == "__main__":
    DirectoryPath="sudesh_Path_Doesnt_exist"
    while(os.path.exists(DirectoryPath)==False):
        DirectoryPath = input("Enter full path of directory to search: ")
        if(os.path.exists(DirectoryPath)==False):
            print(f"Path '{DirectoryPath}' does not exist!")
    print("Search started to find duplicates...")
    Generate_Hashes_Of_Files_And_Search_Duplicates(DirectoryPath)
#    Save_Data_To_JSON_File()
    pause = input("Search Completed. Press any key to continue!!")
