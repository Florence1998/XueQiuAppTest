# 基本的方法：driver，find，click...
from appium.webdriver.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        return self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text
