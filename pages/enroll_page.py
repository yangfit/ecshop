# -*- coding: utf-8 -*-
# @Time : 2020/12/14 14:05
# @Author : fcj11
# @Email : yangfit@126.com
# @File : enroll_page.py
# @Project : ECShop自动化测试
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.home_page import HomePage
from time import sleep


class EnrollPage(BasePage):
    username_locator = (By.ID, 'username')  # 用户名输入框定位
    email_locator = (By.ID, 'email')  # email输入框定位
    password1_locator = (By.ID, 'password1')  # 密码输入框定位
    conform_password_locator = (By.ID, 'conform_password')  # 确认密码输入框定位
    msn_locator = (By.NAME, 'extend_field1')  # msn输入框定位
    qq_locator = (By.NAME, 'extend_field2')  # QQ输入框定位
    office_phone_locator = (By.NAME, 'extend_field3')  # 办公电话输入框定位
    home_phone_locator = (By.NAME, 'extend_field4')  # 家庭电话输入框定位
    mobile_phone_locator = (By.NAME, 'extend_field5')  # 手机输入框定位
    sel_question_locator = (By.NAME, 'sel_question')  # 提示问题下拉框定位
    passwd_answer_locator = (By.NAME, 'passwd_answer')  # 提示问题下拉框定位
    submit_locator = (By.NAME, 'Submit')  # 注册按钮定位

    def input_username(self, username):  # 输入用户名
        self.find_element(self.username_locator).send_keys(username)

    def input_email(self, email):  # 输入email
        self.find_element(self.email_locator).send_keys(email)

    def input_password1(self, password):  # 输入密码
        self.find_element(self.password1_locator).send_keys(password)

    def input_conform_password(self, conform_password):  # 输入确认密码
        self.find_element(self.conform_password_locator).send_keys(conform_password)

    def input_msn(self, msn):  # 输入msn
        self.find_element(self.msn_locator).send_keys(msn)

    def input_qq(self, qq):  # 输入qq
        self.find_element(self.qq_locator).send_keys(qq)

    def input_office_phone(self, office_phone):  # 输入办公电话
        self.find_element(self.office_phone_locator).send_keys(office_phone)

    def input_home_phone(self, home_phone):  # 输入家庭电话
        self.find_element(self.home_phone_locator).send_keys(home_phone)

    def input_mobile_phone(self, mobile_phone):  # 输入手机
        self.find_element(self.mobile_phone_locator).send_keys(mobile_phone)

    def click_sel_question(self):  # 选择第一个密码提示问题
        question = self.find_element(self.sel_question_locator)
        Select(question).select_by_index(1)

    def input_passwd_answer(self, passwd_answer):  # 输入密码提示问题
        self.find_element(self.passwd_answer_locator).send_keys(passwd_answer)

    def click_Submit(self):  # 点击会员注册按钮
        self.find_element(self.submit_locator).click()

    def enroll(self, username, email, password1, conform_password, msn, qq, office_phone, home_phone, mobile_phone,
               passwd_answer):  # 注册过程
        hp = HomePage(self.driver)
        hp.open()
        hp.click_enroll()
        sleep(1)
        self.input_username(username)
        self.input_email(email)
        self.input_password1(password1)
        self.input_conform_password(conform_password)
        self.input_msn(msn)
        self.input_qq(qq)
        self.input_office_phone(office_phone)
        self.input_home_phone(home_phone)
        self.input_mobile_phone(mobile_phone)
        self.click_sel_question()
        self.input_passwd_answer(passwd_answer)
        sleep(1)
        self.click_Submit()
