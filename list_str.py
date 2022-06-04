from pprint import pprint
import os
import glob

base_path = os.getcwd()
path_ = 'sort'
path2 = 'final'
final_file = 'final.txt'
full_path = os.path.join(base_path, path_, path2, final_file)

def sort_file():
    dict_file = {}
    for filename in glob.glob((os.path.join(base_path, path_) + '/*.txt')):
        list_text = []
        with open(filename, 'r', encoding='utf-8') as f:
            quantity = str(sum(1 for line in f))
            dict_file[quantity] = {os.path.basename(filename):list_text}
        with open(filename, 'r', encoding='utf-8') as f:
            list_text = f.readlines()
            dict_file[quantity] = {os.path.basename(filename):list_text}


    sort_dict = sorted(dict_file.items(), key=lambda x: x[0])
    sort_dict = dict(sort_dict)
    pprint(sort_dict)
    with open(full_path, 'w') as endf:
        for qua,val in sort_dict.items():
            for name,text in val.items():
                endf.write(f"{name}\n{qua}\n")
                for l in text:
                    l.strip("'")
                    endf.write(l)
                    endf.write('\n\n')





sort_file()




