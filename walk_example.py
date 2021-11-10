# ****_this is walk example
# ****_Autor: Jakub Koziorowski

# TODO: add multichoice of print usage

import os

total_size = 0
for folder_name, sub_folder_names, file_names in os.walk("C:\\Windows"):
    # print("aktualny folder ", folder_name)
    # for sub_folder in sub_folder_names:
    # print("sub_folder: ", sub_folder)
    for file in file_names:
        current_path = os.path.join(folder_name, file)
        current_size = os.path.getsize(current_path)
        # print("plik: ",current_path," rozmiar: " ,current_size)
        total_size += current_size

print("Total size of Windows [GB]: ", total_size/1024/1024/1024)
