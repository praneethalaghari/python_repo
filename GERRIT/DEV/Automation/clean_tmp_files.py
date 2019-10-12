#!/usr/bin/python

import os
import shutil

tmp_files_dir = "C:/Users/PRANEE~1/AppData/Local/Temp"
os.chdir(tmp_files_dir)

try:
    if len(os.listdir(os.getcwd())) > 0:
        for tmp_file in os.listdir(os.getcwd()):
            if os.path.isfile(tmp_file):
                try:
                    os.remove(tmp_file)
                except:
                    print("Unable to delete file :", tmp_file)
                    pass

            elif os.path.isdir(tmp_file):
                print(tmp_file)
                try:
                    shutil.rmtree(tmp_file)
                except:
                    print("Unable to delete directory :", tmp_file)
                    pass
            else:
                print("content not a file or directory")
except:
    print("There is an unexpected exception!!!")

finally:
    print("There are", len(os.listdir(os.getcwd())) ,"left!!!")