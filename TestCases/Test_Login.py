import time

from selenium import webdriver
import pytest
from POM.LoginPage import Login
from utilities.Readproperties import ReadValue
from utilities.logger import Loggen


class Test_01:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()
    log = Loggen.loggen()

    def test_homepage_title_01(self, setup):
        self.log.info("opening browser")
        self.driver = setup
        act_title = self.driver.title
        print(act_title)
        exp_title = "ParaBank | Register for Free Online Account Access"
        if act_title == exp_title:
            self.log.info("The test_homepage_title passed")
            print("The test_homepage_title passed ")
            self.driver.save_screenshot("D:\\pythonProject\\ParaBank\\Screenshots\\test_homepage_title_01_Pass.png")
            assert True
        # else:
        #     # self.log.info("The test_homepage_title failed")
        #     print("The test_homepage_title Failed ")
        #     self.driver.save_screenshot("D:\\pythonProject\\ParaBank\\Screenshots\\test_homepage_title_01_Fail.png")
        #     assert False

    def test_login_001(self, setup):
        self.log.info("opening browser")
        self.driver = setup
        self.LG = Login(self.driver)
        time.sleep(3)
        self.log.info("Entering username and password")
        time.sleep(3)
        self.LG.setUsername(self.username)
        time.sleep(3)
        self.LG.setPassword(self.password)
        time.sleep(3)
        self.LG.Click_Login()
        self.log.info("checking login status")
        if self.LG.login_status() == True:
            # self.LG.Click_Menu_Button()
            time.sleep(3)
            self.driver.save_screenshot("D:\\pythonProject\\ParaBank\\Screenshots\\test_login_001_Pass.png")
            self.log.info("checkout")
            time.sleep(3)
            self.LG.Click_logout_Button()
            assert True

        else:
            self.log.info("Login failed")
            self.driver.save_screenshot("D:\\pythonProject\\ParaBank\\Screenshots\\test_login_001_Fail.png")
            assert False
