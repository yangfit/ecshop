# -*- coding: utf-8 -*-
# @Time : 2020/12/14 22:04
# @Author : fcj11
# @Email : yangfit@126.com
# @File : read_data.py
# @Project : ECShop自动化测试
from config.configs import DATA_PATH

import xlrd


def read_login_excel(filename=None):  # 从data下面login_data.xls读取登录数据
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/login_data.xls')
    table = data.sheet_by_name('login')
    return [table.row_values(line) for line in range(1, table.nrows)]


def read_enroll_excel(filename=None):  # 从data下面enroll_data.xls读取注册数据
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/enroll_data.xls')
    table = data.sheet_by_name('enroll')
    return [table.row_values(line) for line in range(1, table.nrows)]


def read_add_information_excel(filename=None):  # 从data下面add_information_data.xls读取收货信息数据
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/add_information_data.xls')
    table = data.sheet_by_name('shoppaddress')
    return [table.row_values(line) for line in range(1, table.nrows)]
