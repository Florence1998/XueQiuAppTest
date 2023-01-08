"""雪球首页"""
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from xueqiu.base.xueqiu_app import XueQiuApp
from xueqiu.page.search_page import SearchPage


class MainPage(XueQiuApp):
    _SEARCH_BOX = (AppiumBy.ID, "com.xueqiu.android:id/tv_search")
    _BTN_PENCIL = (AppiumBy.ID, "com.xueqiu.android:id/post_status")

    def click_search(self):
        """点击搜索框，进入搜索页面"""
        # 制造一个弹框，点击【笔】
        self.find_and_click(*self._BTN_PENCIL)
        sleep(0.5)
        # click search box搜索框
        self.find_and_click(*self._SEARCH_BOX)
        return SearchPage(self.driver)
