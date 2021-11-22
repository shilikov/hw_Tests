import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time



LOGIN = ''
PASSWORD = ''
CHROME_DRIVER = ''


class TestYandexAuth(unittest.TestCase):

    @classmethod
    def setupClass(cls: str) -> None:
        print('setupClass create user')

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)

    def test_yandex_auth(self):
        self.driver.get('https://passport.yandex.ru/auth/')

        time.sleep(1)

        login_input = self.driver.find_element_by_name('login')
        login_input.send_keys(LOGIN)
        login_input.submit() # https://stackoverflow.com/questions/17530104/selenium-webdriver-submit-vs-click

        time.sleep(1)

        password_input = self.driver.find_element_by_name('passwd')
        password_input.send_keys(PASSWORD)
        password_input.submit()

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls: str) -> None:
        print("tearDownClass 123")

