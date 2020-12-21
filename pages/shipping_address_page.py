# -*- coding: utf-8 -*-
# @Time : 2020/12/14 22:27
# @Author : fcj11
# @Email : yangfit@126.com
# @File : Shipping_address_page.py
# @Project : ECShop自动化测试
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from time import sleep


class ShoppAddress(BasePage):
    myaccount_locator = (By.XPATH, '/html/body/div[1]/div/div/a[1]')  # 定位我的账户入口
    shoppaddress_locator = (
        By.CSS_SELECTOR, 'body > div.block.clearfix > div.AreaL > div > div > div > div > a:nth-child(4)')  # 定位收货地址
    country_locator = (By.NAME, 'country')  # 定位国家下拉框
    province_locator = (By.NAME, 'province')  # 定位省份
    city_locator = (By.NAME, 'city')  # 定位城市
    district_locator = (By.NAME, 'district')  # 定位区域
    consignee_locator = (By.NAME, 'consignee')  # 定位收货人姓名输入框
    address_locator = (By.NAME, 'address')  # 定位详细地址
    tel_locator = (By.NAME, 'tel')  # 定位电话输入框
    email_locator = (By.NAME, 'email')  # 定位电子邮箱地址输入框
    submit_locator = (By.NAME, 'submit')  # 定位新增收货地址按钮

    def click_myaccount(self):  # 点击我的账户
        self.find_element(self.myaccount_locator).click()

    def click_shoppaddress(self):  # 点击收货地址添加
        self.find_element(self.shoppaddress_locator).click()

    def click_country(self):  # 选择国家第一个
        Select(self.find_element(self.country_locator)).select_by_index(1)

    def click_province(self):  # 选择第一个省份
        Select(self.find_element(self.province_locator)).select_by_index(1)

    def click_city(self):  # 选择第一个城市
        Select(self.find_element(self.city_locator)).select_by_index(1)

    def click_district(self):  # 选择第一个区县
        Select(self.find_element(self.district_locator)).select_by_index(1)

    def input_consignee(self, consignee):  # 输入收货人姓名
        self.find_element(self.consignee_locator).clear()
        sleep(0.5)
        self.find_element(self.consignee_locator).send_keys(consignee)

    def input_address(self, address):  # 输入详细地址
        self.find_element(self.address_locator).clear()
        sleep(0.5)
        self.find_element(self.address_locator).send_keys(address)

    def input_tel(self, tel):  # 输入电话
        self.find_element(self.tel_locator).clear()
        sleep(0.5)
        self.find_element(self.tel_locator).send_keys(tel)

    def input_email(self, email):  # 输入email
        self.find_element(self.email_locator).clear()  # 清空输入框
        sleep(0.5)
        self.find_element(self.email_locator).send_keys(email)

    def click_submit(self):  # 点击提交订单
        self.find_element(self.submit_locator).click()

    def add_information(self, consignee, address, tel, email):  # 新增收货地址

        self.click_shoppaddress()  # 点击收货地址，进入到收货信息填写
        sleep(0.5)
        self.click_country()  # 选择国家
        sleep(0.5)
        self.click_province()  # 选择省份
        sleep(0.5)
        self.click_city()  # 选择城市
        sleep(0.5)
        self.click_district()  # 选择区县
        sleep(0.5)
        self.input_consignee(consignee)  # 输入收货人信息
        sleep(0.5)
        self.input_address(address)  # 输入详细地址
        sleep(0.5)
        self.input_tel(tel)  # 输入电话
        sleep(0.5)
        self.input_email(email)  # 输入email
        sleep(0.5)
        self.click_submit()  # 点击提交
