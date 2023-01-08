# 基本的方法：driver，find，click...
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from xueqiu.base.black_handle import black_wrapper


class BasePage(object):

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # def find(self, by, locator):
    #     try:
    #         return self.driver.find_element(by, locator)
    #     except Exception as e:
    #         print("未找到元素，处理异常")
    #         for black in self.black_list:
    #             # 查找黑名单中的每一个元素
    #             eles = self.driver.find_elements(*black)
    #             if len(eles) > 0:
    #                 # 点掉弹框
    #                 eles[0].click()
    #                 # 继续查找元素
    #                 return self.find(by, locator)
    #         raise e

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        return self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text

    def screenshot(self, name):
        # 截图
        self.driver.save_screenshot(name)
