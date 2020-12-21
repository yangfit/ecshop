# -*- coding: utf-8 -*-
# @Time : 2020/12/14 17:02
# @Author : fcj11
# @Email : yangfit@126.com
# @File : shoppingcar_page.py
# @Project : ECShop自动化测试
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class ShoppingCar(BasePage):
    go_on_shopping_locator = (By.CSS_SELECTOR,
                              'body > div.block.table > div.flowBox > table > tbody > tr > td:nth-child(1) > a > img')  # 继续购物按钮定位
    clear_cart_locator = (
    By.CSS_SELECTOR, '#formCart > table:nth-child(2) > tbody > tr > td:nth-child(2) > input:nth-child(1)')  # 清空购物车按钮定位
    settlement_center_locator = (By.CSS_SELECTOR,
                                 'body > div.block.table > div.flowBox > table > tbody > tr > td:nth-child(2) > a > img')  # 结算中心按钮定位
    submit_locator = (
    By.CSS_SELECTOR, '#theForm > div > table > tbody > tr:nth-child(6) > td > input.bnt_blue_2')  # 定位配送至这个地址

    def click_go_on_shopping(self):  # 点击继续购物按钮
        self.find_element(self.go_on_shopping_locator).click()

    def click_Clear_cart(self):  # 点击清空购物车按钮
        self.find_element(self.clear_cart_locator).click()

    def click_settlement_center(self):  # 点击结算中心
        self.find_element(self.settlement_center_locator).click()

    def click_submit(self):  # 点击配送这个地址
        self.find_element(self.submit_locator).click()

    def settlement_center(self):  # 结算中心过程

        self.click_settlement_center()
        sleep(1)
        self.click_submit()
