# -*- coding: utf-8 -*-
# @Time : 2020/12/14 13:52
# @Author : fcj11
# @Email : yangfit@126.com
# @File : cehsi.py
# @Project : ECShop自动化测试
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.1.161/upload/admin')
driver.find_element(By.NAME,'username').send_keys('nichao')
driver.find_element(By.NAME,'password').send_keys('nichao123456')
driver.find_element(By.CSS_SELECTOR,'body > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(2) > input').click()
sleep(1)
driver.switch_to.frame("header-frame")
sleep(1)
driver.find_element(By.CSS_SELECTOR,'#menu-div > ul > li:nth-child(5) > a').click()
sleep(1)
driver.switch_to.parent_frame()
sleep(1)
driver.switch_to.frame('main-frame')






#
def row_cell_get_table_text(table_loc, row ,cell):
    cell = str(cell)
    row = str(row + 1)
    locator = f"{table_loc}/tbody/tr[{row}]/td[{cell}]"
    # text = driver.find_element_by_xpath(locator).text
    text = driver.find_element(By.XPATH,locator).text

    return text.splitlines()[1]

text = row_cell_get_table_text("//*[@id='listDiv']/table[1]",2,3)
print(text)



# //*[@id="listDiv"]/table[1]/tbody/tr[3]/td[3]

sleep(1)


driver.quit()
