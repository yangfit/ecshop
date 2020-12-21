# -*- coding: utf-8 -*-
# @Time : 2020/12/14 21:27
# @Author : fcj11
# @Email : yangfit@126.com
# @File : submitorder_page.py
# @Project : ECShop自动化测试

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SubmitTorder(BasePage):
    deliver_locator = (By.NAME, 'shipping')  # 定位上门取货
    payment_locator = (By.NAME, 'payment')  # 定位支付宝支付方式
    submit_locator = (
        By.CSS_SELECTOR, '#theForm > div:nth-child(12) > div:nth-child(3) > input[type=image]:nth-child(1)')  # 定位提交订单按钮

    def click_deliver(self):  # 选择上门取货
        self.find_element(self.deliver_locator).click()

    def click_payment(self):  # 选支付宝支付
        self.find_element(self.payment_locator).click()

    def click_submit(self):  # 点击提交订单按钮
        self.find_element(self.submit_locator).click()

    def submit_torder(self):  # 提交订单流程

        self.click_deliver()
        self.click_payment()
        self.click_submit()
