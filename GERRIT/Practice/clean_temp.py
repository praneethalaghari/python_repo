import os
import shutil

dir = 'C:/Users/PRANEE~1/AppData/Local/Temp'

if len(os.listdir(dir)) == 0:
    print('No Temp files found!!!')
else:    
    print('Number of temp files/folders',len(os.listdir(dir)))
    dir_list = os.listdir(dir)
    for f in dir_list:
        try:
            os.chdir(dir) #This should be done only if path is not appnd to file
            file_folder_to_remove = os.path.join(dir,f) 
            if not os.path.isdir(file_folder_to_remove):
                os.remove(f)
            else:
                if len(os.listdir(f)) ==0:
                    os.rmdir(f)
                else:
                    shutil.rmtree(f)
        except FileNotFoundError:
            print('File is not found or reachable')
            continue
        except PermissionError:
            print('File \'' + f + '\' cannot be deleted due to permissions')
            continue

