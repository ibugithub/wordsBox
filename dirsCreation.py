import os
import shutil 

src_dir = os.getcwd()
src_name = "samplewordsBox"
src_path = os.path.join(src_dir, src_name)
dest_dir = os.getcwd()


def fileCreation(last_alphabet, alpha_range, value):
    for i in range(1, alpha_range + 1):
        folder_name = chr(ord(last_alphabet) + i) + src_name[6:]
        folder_path = os.path.join(dest_dir, folder_name)
        if value == 'delete':
            shutil.rmtree(folder_path) 
            continue
        shutil.copytree(src_path, folder_path)
        with os.scandir(os.getcwd()) as dir: 
            for folder in dir: 
                if folder.name == folder_name:
                    j = 1
                    for fol in os.listdir(folder):
                        current_name = os.getcwd() + '/' + folder_name + '/' + fol
                        new_name = os.getcwd() + '/' + folder_name + '/' + folder_name + str(j)
                        os.rename(current_name, new_name)   
                        j += 1





# first perameter "D" is for creating folder by the next latter after D 
# second perameter 1 is for how many dirs you want to create by the name after the D latter
# Set create to create dirs or set delete to delete dirs
fileCreation('E', 4, 'create')
