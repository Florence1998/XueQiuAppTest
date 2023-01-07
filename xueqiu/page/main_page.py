"""雪球首页"""
from appium.webdriver.common.appiumby import AppiumBy
from xueqiu.base.xueqiu_app import XueQiuApp
from xueqiu.page.search_page import SearchPage


class MainPage(XueQiuApp):
    _SEARCH_BOX_ELEMENT = (AppiumBy.ID, "com.xueqiu.android:id/tv_search")

    def click_search(self):
        """点击搜索框，进入搜索页面"""
        self.find_and_click(*self._SEARCH_BOX_ELEMENT)
        return SearchPage(self.driver)
