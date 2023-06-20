from selenium.webdriver.common.by import By
from selenium import webdriver


class Register:
    click_link_Register_xpath = (By.XPATH, "//a[normalize-space()='Register']")

    text_Firstname_Name = (By.NAME, "customer.firstName")
    text_Lastname_Name = (By.NAME, "customer.lastName")
    text_ADress_Name = (By.NAME, "customer.address.street")
    text_ADressCity_Name = (By.NAME, "customer.address.city")
    text_ADressState_Name = (By.NAME, "customer.address.state")
    text_ADressZip_Name = (By.NAME, "customer.address.zipCode")
    text_ADressPhone_Name = (By.NAME, "customer.phoneNumber")
    text_ADressSSn_Name = (By.NAME, "customer.ssn")

    text_Username_Name = (By.NAME, "customer.username")
    text_Password_Name = (By.NAME, "customer.password")
    text_RepeatedPasswd_Name = (By.NAME, "repeatedPassword")
    click_login_Reg_xpath = (By.XPATH, "//input[@value='Register']")

    def __init__(self, driver):
        self.driver = driver

    def click_Register_login(self):
        self.driver.find_element(self.click_link_Register_xpath).click()

    def Firstname_Name(self, Firstname):
        self.driver.find_element(self.text_Firstname_Name).send_keys(Firstname)

    def Lastname_Name(self, Lastname):
        self.driver.find_element(self.text_Lastname_Name).send_keys(Lastname)

    def ADress_Name(self, ADress):
        self.driver.find_element(self.text_ADress_Name).send_keys(ADress)

    def ADressCity_Name(self, ADressCity):
        self.driver.find_element(self.text_ADressCity_Name).send_keys(ADressCity)

    def ADressState_Name(self, ADressState):
        self.driver.find_element(self.text_ADressState_Name).send_keys(ADressState)

    def ADressZip_Name(self,ADressZip):
        self.driver.find_element(self.text_ADressZip_Name).send_keys(ADressZip)

    def ADressPhone_Name(self, ADressPhone):
        self.driver.find_element(self.text_ADressPhone_Name).send_keys(ADressPhone)

    def ADressSSn_Name(self, ADressSSn):
        self.driver.find_element(self.text_ADressSSn_Name).send_keys(ADressSSn)

    def Username_Name(self, Username):
        self.driver.find_element(self.text_Firstname_Name).send_keys(Username)

    def Password_Name(self, Password):
        self.driver.find_element(self.text_Firstname_Name).send_keys(Password)

    def RepeatedPasswd_Name(self, RepeatedPasswd):
        self.driver.find_element(self.text_Password_Name).send_keys(RepeatedPasswd)

    def click_login_Reg(self):
        self.driver.find_element(self.click_login_Reg_xpath).click()
