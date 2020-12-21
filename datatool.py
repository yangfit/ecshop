# -*- coding: utf-8 -*-
# @Time : 2020/12/11 19:27
# @Author : nichao
# @Email : 530504026@qq.com
# @File : datatool.py
# @Project : page
import xlrd
from config.configs import DATA_PATH
def logindata(filename= None):
    if not filename:
        filename=DATA_PATH
    data=xlrd.open_workbook(filename)
    table=data.sheet_by_name("login")
    data_list=[]
    for n_row in range(1,table.nrows):
        data_list.append(table.row_values(n_row))
    return data_list
print(logindata())
