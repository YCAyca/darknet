
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:58:41 2020

@author: yagmur
"""
import os 

imgDir = "..\\dataset_redbull\\train\\"

train_file = "..\\dataset_redbull\\train.txt"

train = open(train_file, "w+")


for imgName in os.listdir(imgDir):
    if imgName == "desktop.ini":
        continue
    if imgName.split('.')[1] != 'txt':
        string_1 = "C:\\Users\\aktas\\Desktop\\Object_Recognition\\dataset_redbull\\train\\" 
        string_2 = imgName
        yaz = string_1 + string_2
        print(yaz)
        train.write(str((yaz).encode('utf8')))
train.close()