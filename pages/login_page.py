# -*- coding: utf-8 -*-
# @Time : 2020/12/14 16:20
# @Author : fcj11
# @Email : yangfit@126.com
# @File : login_page.py
# @Project : ECShop自动化测试

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
from time import sleep


class Loginpage(BasePage):
    homepage_locator = (By.CSS_SELECTOR, 'body > div.menu_box.clearfix > div > div > a.cur')  # 定位首页按钮
    username_locator = (By.NAME, 'username')  # 定位用户名输入框
    password_locator = (By.NAME, 'password')  # 定位密码输入框
    submit_locator = (By.NAME, 'submit')  # 定位登录点击按钮
    commodity_locator = (By.XPATH, '/html/body/div[9]/div[3]/div[1]/div/ul[1]/li[1]/a/img')  # 商品定位
    buy_locator = (By.XPATH, '//*[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img')  # 定位立即购买按钮
    shopping_car_locator = (By.CSS_SELECTOR, '#ECS_CARTINFO > a')  # 查看购物车按钮定位

    def input_username(self, username):  # 输入用户名
        self.find_element(self.username_locator).send_keys(username)

    def input_password(self, password):  # 输入密码
        self.find_element(self.password_locator).send_keys(password)

    def click_submit(self):  # 点击登录按钮
        self.find_element(self.submit_locator).click()

    def click_hmepage(self):  # 点击首业按钮
        self.find_element(self.homepage_locator).click()

    def click_commodity(self):  # 点击商品
        self.find_element(self.commodity_locator).click()

    def click_buy(self):  # 点击立即购买按钮
        self.find_element(self.buy_locator).click()

    def click_shopping_car(self):  # 点击查看购物车按钮
        self.find_element(self.shopping_car_locator).click()

    def login(self, username, password):
        hp = HomePage(self.driver)
        hp.open()
        hp.click_login()
        sleep(1)
        self.input_username(username)
        self.input_password(password)
        self.click_submit()
        sleep(3)

    def buy(self):
        self.click_hmepage()
        sleep(2)
        self.click_commodity()
        self.click_buy()
