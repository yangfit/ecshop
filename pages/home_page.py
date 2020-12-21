# -*- coding: utf-8 -*-
# @Time : 2020/12/11 15:12
# @Author : nichao
# @Email : 530504026@qq.com
# @File : loginpag.py
# @Project : page
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    _url = BasePage._url + "/upload"  # 前台主页面地址

    enroll_locator = (By.CSS_SELECTOR, '#ECS_MEMBERZONE > a:nth-child(2)')  # 注册入口定位(enroll_locator)
    login_locator = (By.XPATH, '//*[@id="ECS_MEMBERZONE"]/a[1]')  # 登录入口定位(login_locator)

    def open(self):
        self.driver.get(self.url)

    def click_enroll(self):  # 点击注册
        self.find_element(self.enroll_locator).click()

    def click_login(self):  # 点击登录
        self.find_element(self.login_locator).click()
