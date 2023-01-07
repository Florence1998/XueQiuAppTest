"""搜索页面"""
from appium.webdriver.common.appiumby import AppiumBy
from xueqiu.base.xueqiu_app import XueQiuApp
from xueqiu.page.search_result_page import SearchResultPage


class SearchPage(XueQiuApp):
    _SEARCH_BOX = (AppiumBy.ID, "com.xueqiu.android:id/search_input_text")

    def input_search_content(self, searchkey):
        """向搜索输入框中输入【alibaba】"""
        # input search content
        self.find_and_send(*self._SEARCH_BOX, searchkey)
        return self

    def click_search_result(self, text):
        """点击搜索结果中的【阿里巴巴】"""
        # click 搜索结果
        self.find_and_click(AppiumBy.XPATH, f"//*[@text='{text}']")
        return SearchResultPage(self.driver)
