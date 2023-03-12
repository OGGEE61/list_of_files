import os

#path for the program is currently set to current working directory
file_path = os.getcwd()

for folder, sub_folders, files in os.walk(file_path):
    
    print(f"Currently looking at {folder}")
    print('\n')
    print('The subfodlers are: ')
    for sub_fold in sub_folders:
          print(f"\t Subfolder: {sub_fold}")
            
    print('\n')
    print('The files are: ')
    for f in files:
        print(f'\t File: {f}')
    print('\n')
          