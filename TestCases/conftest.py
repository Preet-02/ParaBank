import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    driver.maximize_window()
    return driver


# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("launching chrome browser")
#     elif browser == 'firefox':
#         driver = webdriver.firefox()
#     elif browser == 'edge':
#         driver = webdriver.edge()
#     elif browser == 'IE':
#         driver = webdriver.ie()
#     else:
#         chrome_opt = webdriver.ChromeOptions()
#         chrome_opt.add_argument('headless')
#         driver = webdriver.Chrome(options=chrome_opt)
#     driver.maximize_window()
#     return driver
#
#     ret
