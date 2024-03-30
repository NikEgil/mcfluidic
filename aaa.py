import os
import numpy as np
from natsort import natsorted
import matplotlib
import matplotlib.pyplot as plt
import re
import pandas as pd
from scipy import signal




start_nm = 400  # нм
end_nm = 700  # нм

x = pd.read_excel("x points nm.xlsx")
x = np.array(x["nm"].values[1 : len(x) - 1])

def nm_to_x(nm):
    return xint.index(nm) + 1

def x_to_nm(index):
    return x[index]
# номера точек в массиве по координате х
for i in range(len(x)):
    if x[i] > start_nm:
        start_x = i
        break
for i in range(len(x) - 1, 0, -1):
    if x[i] < end_nm:
        end_x = i
        break
x = x[start_x:end_x]
xint = list(np.array(x, dtype=int))
tail_x = nm_to_x(650)
head_x = nm_to_x(475)



def get_data_rmr(path):
    """получение всей папки в виде списка с массивами np"""
    _file_list = np.array(natsorted(os.listdir(path)))
    _data = []
    for file in range(len(_file_list)):
        with open(path + _file_list[file], "r", encoding="utf8") as spec:
            spec = re.split(",", spec.read())
            _data.append(np.array(spec[start_x:end_x], dtype=float))
    #    _data.append(get_rmr(spec))
    return _data

data_row = []  # изанчальные графики
data = []  # сглаженные графики
smooth = True
main_folder = r"C:\Users\Nik\Desktop\скр2\points\p0-2"
main_folder = main_folder.replace(chr(92), "/")
folders_list = list(natsorted(os.listdir(main_folder)))
print(main_folder)
print(folders_list)


for i in range(len(folders_list)):
    data_row.append(get_data_rmr(main_folder + "/" + folders_list[i] + "/"))
    print(folders_list[i], " recived ", len(data_row[i]))


if smooth == True:
    for i in range(len(data_row)):
        d = []
        for j in range(len(data_row[i])):
            d.append(signal.savgol_filter(data_row[i][j], 60, 3))
        data.append(d)
else:
    data = data_row.copy()
print("получено " + str(len(data_row)) + " папок")



для сглаживания использовать лучше это:
 smooth_massiv=signal.savgol_filter(massiv,100,3)