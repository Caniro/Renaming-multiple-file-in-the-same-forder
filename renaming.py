import os
import math

def get_digits(num):
    if num == 0:
        return 1
    return (int(math.log10(num)) + 1)

def rename_multiple_files():
    folder_path = "."
    target_extension = ".png"

    file_list = os.listdir(folder_path)
    if len(file_list) == 0:
        return
    digits = int(math.log10(len(file_list))) + 1
    
    count = 0
    for file in file_list:
        file_extension = os.path.splitext(file)[1]
        if file_extension != target_extension:
            continue
        filename = str(count)
        num_of_prefix = digits - get_digits(count)
        if (num_of_prefix > 0):
            filename = '0' * num_of_prefix + filename
        os.rename(folder_path + "\\" + file, \
                  folder_path + "\\" + filename + file_extension)
        count += 1
    print("Complete!")

if __name__ == '__main__':
    rename_multiple_files()
