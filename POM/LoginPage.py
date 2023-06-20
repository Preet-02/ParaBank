from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Login:
    Text_username_Name = (By.NAME, "username")
    Text_Password_Name = (By.NAME, "password")
    Click_Login_Xpath = (By.XPATH, "//input[@value='Log In']")
    Click_menu_Xpath = (By.XPATH, "//a[normalize-space()='home']")
    Click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Log Out']")

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(*Login.Text_username_Name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*Login.Text_Password_Name).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Login.Click_Login_Xpath).click()

    def login_status(self):
        try:
            # self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
            self.driver.find_element(*Login.Click_menu_Xpath)
            return True
        except NoSuchElementException:
            return False

    def Click_Menu_Button(self):
        # self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
        self.driver.find_element(*Login.Click_menu_Xpath).click()

    def Click_logout_Button(self):
        self.driver.find_element(*Login.Click_Logout_Xpath).click()



