import os
from operator import itemgetter
import shutil

def only_txt_files(directory):
    """ this func find all txt files """
    txt_files = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files

def txt_merge(new_file_name):
    """ 
    sort all txt files by len, and merge them with 2 service lines
    first with name of merged file
    and second with numbers of lines in it
                                                                         """
    try:
        os.remove(os.getcwd() + "\\" + "some txt" + "\\" + new_file_name)
    except:
        pass
    list_of_len_txt = []
    for file in only_txt_files(os.chdir(r"some txt")):
        with open(file, "r", encoding="UTF-8") as f: # make list with len of .txt files
            list_of_len_txt.append(len(f.read())) 
    sort_list_of_len = []
    for idx, qty in enumerate(list_of_len_txt): # numerate them and sort
        sort_list_of_len.append([idx, qty])
    sort_list_of_len.sort(key=itemgetter(1))
    for list_ in sort_list_of_len:
        y = list_[0]
        file = only_txt_files(os.getcwd())[y] 
        with open(file, "r", encoding="UTF-8") as fr, open(new_file_name, "a+", encoding="UTF-8" ) as fw:
            text = fr.read() # create new file with service lines and information 
            x = text.count("\n") +1
            fw.write(fr.name + "\n")
            fw.write(str(x) + "\n")
            fw.write(text + "\n")
    print("Файл успешно создан")


txt_merge("test.txt")


    