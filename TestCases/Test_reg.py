import time

from selenium import webdriver
import pytest
from POM.Register import Register


class Test_01:
    Firstname = "Namrata"
    Lastname = "Karale"
    ADress = "Ram Temple"
    ADressCity = "Nagpur"
    ADressState = "Maharashtra"
    ADressZip = "440024"
    ADressPhone = "9423645776"
    ADressSSn = "1233"
    Username = "NamrataP"
    Password = "Namrata90"
    RepeatedPasswd = "Namrata90"

    @pytest.mark.skip
    def test_homepage_title_01(self, setup):
        self.driver = setup
        act_title = self.driver.title
        print(act_title)
        exp_title = "ParaBank | Register for Free Online Account Access"
        if act_title == exp_title:
            print("The test_homepage_title passed ")
            self.driver.save_screenshot("D:\\pythonProject\\ParaBank\\Screenshots\\test_homepage_title_01_Pass.png")
            assert True
        else:
            print("The test_homepage_title Failed ")
            self.driver.save_screenshot("D:\\pythonProject\\ParaBank\\Screenshots\\test_homepage_title_01_Fail.png")
            assert False

    @pytest.mark.skip
    def test_register_01(self, setup):
        self.driver = setup
        self.RG = Register(self.driver)
        time.sleep(3)
        self.RG.click_Register_login()
        self.RG.Firstname_Name(self.Firstname)
        self.RG.Lastname_Name(self.Lastname)
        self.RG.ADress_Name(self.ADress)
        self.RG.ADressCity_Name(self.ADressCity)
        self.RG.ADressState_Name(self.ADressState)
        self.RG.ADressZip_Name(self.ADressZip)
        self.RG.ADressSSn_Name(self.ADressSSn)
        self.RG.Username_Name(self.Username)
        self.RG.Password_Name(self.Password)
        self.RG.RepeatedPasswd_Name(self.RepeatedPasswd)
        self.RG.click_login_Reg()
