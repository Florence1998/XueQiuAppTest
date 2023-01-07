# app相关的操作：雪球应用的启动start， 重启restart，停止stop
from appium import webdriver

from xueqiu.base.base_page import BasePage


class XueQiuApp(BasePage):
    def start(self):
        if self.driver == None:
            print("driver == None")
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "6.0"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"  # 保留登录信息（缓存），不写的话执行时会清缓存，清掉登录信息
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(15)
        else:
            # 直接启动
            print("复用driver")
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        from xueqiu.page.main_page import MainPage
        return MainPage(self.driver)
