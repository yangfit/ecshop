# -*- coding: utf-8 -*-
# @Time : 2020/12/11 15:21
# @Author : nichao
# @Email : 530504026@qq.com
# @File : base_page.py
# @Project : page

class BasePage():
    _url = "http://192.168.1.161"

    def __init__(self, driver, url=None):
        self.driver = driver
        if not url:
            url = self._url
        self.url = url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
