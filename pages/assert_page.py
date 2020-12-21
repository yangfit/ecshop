# -*- coding: utf-8 -*-
# @Time : 2020/12/15 15:32
# @Author : fcj11
# @Email : yangfit@126.com
# @File : assert_page.py
# @Project : ECShop自动化测试
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class Assert(BasePage):
    _url = BasePage._url + '/upload/admin/'  # 后台登录地址

    uername_locator = (By.NAME, 'username')  # 定位用户名输入框
    password_locator = (By.NAME, 'password')  # 定位密码输入框
    submit_locator = (By.CSS_SELECTOR,  # 定位进入管理中心按钮
                      'body > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(2) > input')
    order_management_locator = (By.CSS_SELECTOR, '#menu-div > ul > li:nth-child(5) > a > span:nth-child(2)')  # 定位订单管理

    def input_username(self):  # 输入框输入用户名
        self.find_element(self.uername_locator).send_keys('nichao')

    def input_password(self):  # 输入框输入密码
        self.find_element(self.password_locator).send_keys('nichao123456')

    def clicn_submit(self):  # 点击进入管理员中心按钮
        self.find_element(self.submit_locator).click()

    def click_order_management(self):
        self.find_element(self.order_management_locator).click()

    def open(self):
        self.driver.get(self.url)

    def get_assert_text(self, table_loc, row, cell):
        self.open()
        self.input_username()
        self.input_password()
        self.clicn_submit()
        sleep(1)
        self.driver.switch_to.frame("header-frame")
        sleep(1)
        self.click_order_management()
        sleep(1)
        self.driver.switch_to.parent_frame()
        sleep(1)
        self.driver.switch_to.frame('main-frame')
        sleep(1)
        cell = str(cell)
        row = str(row + 1)
        locator = f"{table_loc}/tbody/tr[{row}]/td[{cell}]"
        text = self.driver.find_element_by_xpath(locator).text

        return text.splitlines()[1]
