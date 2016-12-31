# coding: utf-8
import sys
import os

#gather arguments to pass to rename_files
path = str(sys.argv[1])
prefix = str(sys.argv[2])

#define function

def rename_files(path, prefix):
    
    #save current directory to return to later
    current_directory = os.getcwd()
    
    #change to the target directory
    os.chdir(path)
    
    #if the path is correct list all the containing files
    file_list = os.listdir(path)
    
    #init the counter
    
    count = 0;

    for file_name in file_list:
        #break apart each string at the . for file extention
        scrub = file_name.split(".")
        extention = scrub[1]
        
        #for all passing if statement rename based on provided prefix and reatach correct extention
        if extention != "DS_Store":
           count = count + 1
           os.rename(file_name, prefix + "-" + str(count) + "." + extention)

        #return to originla directory

    os.chdir(current_directory)
    
rename_files(path, prefix)
