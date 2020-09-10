#****_this is walk example
#****_Autor: Jakub Koziorowski

# TODO: add multichoice of print usage

import os

total_size = 0
for folder_name, subfolder_names, file_names in os.walk("C:\\Windows"):
    #print("aktualny folder ", folder_name)
    #for subfolder in subfolder_names:
        #print("subfolder: ", subfolder)
    for file in file_names:
        current_path = os.path.join(folder_name, file)
        current_size = os.path.getsize(current_path)
        #print("plik: ",current_path," rozmiar: " ,current_size)
        total_size += current_size

print("Total size of Windows [GB]: ", total_size/1024/1024/1024)