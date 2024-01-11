#!/usr/bin/env python.exe

# This code is for converting xpt file to csv file

# -----------------------------------------------------------------------------
# Date                     Programmer
# ----------   --------------------------------------------------------------
# Jan-10-2024    Md Yousuf Ali (md.ali@fda.hhs.gov)

# import os
# import pathlib
# import glob
# import pandas as pd
# import pyreadstat

xpt_path = 'C:/Users/Md.Ali/OneDrive - FDA/yousuf/10_DATA/Biocelerate_shared_data/data/'
# where_to_save = pathlib.Path(xpt_path,'data_save')
# where_to_save.exists()
# where_to_save.is_dir()
# where_to_save.mkdir()
# 1MDogA_send
# 1MDogB_send
# 1MDogB_send
# 1MRatB_send

# read xpt file
# df, meta = pyreadstat.read_xport('bw.xpt')


# write to csv file
# df.to_csv('bw.csv', index= False, encoding = 'utf-8')

import pathlib
import pyreadstat
import pandas as pd

def xpt_to_csv(xpt_path, where_to_save):

    # if pathlib.Path(xpt_path).exists() and pathlib.Path(where_to_save).exists():

    # else:
        # print('file or directory does not exits')
    if pathlib.Path(xpt_path).is_file():
        df, meta = pyreadstat.read_xport(xpt_path)
        file_name = pathlib.Path(xpt_path).stem
        file_name = file_name + '.csv'
        path_to_save = pathlib.Path(where_to_save, file_name)
        df.to_csv(path_to_save)
    else:

        if pathlib.Path(xpt_path).is_dir():
            path_x = pathlib.Path(xpt_path)
            all_xpt = [i for i in path_x.rglob('*.xpt')]
            unq_dir = set([i.parent.name for i in all_xpt])
            breakpoint()
            dir_save = []
            for i in unq_dir:
                k = pathlib.Path(where_to_save, i)
                if k not in dir_save:
                    dir_save.append(k)
                k.mkdir(exist_ok=True)
            for i in all_xpt:
                file_name = i.stem + '.csv'
                df, meta = pyreadstat.read_xport(i)
                final_path = i.parent.name

                save_to = pathlib.Path(where_to_save, final_path, file_name)
                df.to_csv(save_to)





phuse_xpt = 'C:/Users/Md.Ali/OneDrive - FDA/yousuf/00_github_projects/phuse-scripts/data/send/'
save_file = 'C:/Users/Md.Ali/OneDrive - FDA/yousuf/00_github_projects/xpt_convert/phuse_test'

xpt_to_csv(xpt_path= phuse_xpt, where_to_save= save_file )

pathlib.Path(phuse_xpt).is_file()


os.listdir(xpt_path)
p = pathlib.Path(__file__)
print(p)

pathlib.Path.cwd()
pathlib.Path.home()




p = pathlib.Path(xpt_path)
p.exists()

p.is_dir()
p.is_file()

print(p)
pathlib.PurePath(xpt_path)
pathlib.PurePath('to_csv.py').parent()

p = pathlib.Path(xpt_path).iterdir()
for i in p:
    # k = pathlib.PurePath(i)
    print(i)

path = pathlib.Path(xpt_path)
for f in path.rglob('*.xpt'):
    print(f)

all_xpt = [i for i in path.rglob('*.xpt')]
print(all_xpt)

set([i.parent for i in all_xpt])
path.owner

all_xpt[]
dir_create = []
for i in all_xpt[0:90:10]:
    print(i.name)
    print(i.parent.name)
    k = i.parent.name
    if k not in dir_create:
        dir_create.append(k)

print(dir_create)
for i in dir_create:
    k = pathlib.Path(where_to_save, i)
    k.mkdir(exist_ok=True)



for i in all_xpt[0:10]:
    df,meta = pyreadstat.read_xport(i)
    print(df.head())

all_xpt_parent = [i.parent for i in path.rglob('*.xpt')]

unq_xpt_path = set(all_xpt_parent)
for i in unq_xpt_path:
    print(i)
print(unq_xpt_path)
len(unq_xpt_path)





# df = pyreadstat.read_xport('bw.xpt')


# done! let's see what we got
# print(df.head())
# print(meta.column_names)
# print(meta.column_labels)
# print(meta.column_names_to_labels)
# print(meta.number_rows)
# print(meta.number_columns)
# print(meta.file_label)
# print(meta.file_encoding)

# meta.original_variable_types

# meta.readstat_variable_types

# meta.variable_display_width
# meta.variable_to_label

# df.head()
# type(df)
