# -*- coding: utf-8 -*-
# @Time : 2020/12/10 19:08
# @Author : nichao
# @Email : 530504026@qq.com
# @File : case.py
# @Project : page
import unittest
from time import sleep
from cases.base_case import BaseCase
from pages.enroll_page import EnrollPage
from pages.login_page import Loginpage
from pages.shoppingcar_page import ShoppingCar
from pages.submitorder_page import SubmitTorder
from pages.shipping_address_page import ShoppAddress
from model.read_data import read_enroll_excel, read_add_information_excel, read_login_excel
from pages.assert_page import Assert


class MyTest(BaseCase):

    def test_1(self):
        """用户注册 - 添加收货地址 - 添加购物车 - 订单 - 结算"""
        # 注册用户
        username, email, password1, conform_password, msn, qq, office_phone, home_phone, mobile_phone, passwd_answer = \
            read_enroll_excel()[2]  # 提取数据
        EnrollPage(self.driver).enroll(username, email, password1, conform_password, msn, int(qq), int(office_phone),
                                       int(home_phone),
                                       int(mobile_phone), passwd_answer)
        # 添加收货信息
        onsignee, address, tel, email = read_add_information_excel()[1]
        ShoppAddress(self.driver).add_information(onsignee, address, int(tel), email)

        # 添加购物车
        Loginpage(self.driver).buy()
        sleep(2)

        # 生成订单
        ShoppingCar(self.driver).settlement_center()
        sleep(1)

        # 提交订单
        SubmitTorder(self.driver).submit_torder()
        sleep(3)

        a = Assert(self.driver)  # 断言
        text = a.get_assert_text("//*[@id='listDiv']/table[1]", 2, 3)
        self.assertEqual(address, text, '提交订单失败')

    def test_2(self):  #登录
        admin, password = read_login_excel()[0]
        Loginpage(self.driver).login(admin, password)


if __name__ == '__main__':
    unittest.main()
