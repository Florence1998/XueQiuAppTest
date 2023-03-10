"""搜索结果页"""
from appium.webdriver.common.appiumby import AppiumBy
from xueqiu.base.xueqiu_app import XueQiuApp


class SearchResultPage(XueQiuApp):
    _MENU_STOCK = (AppiumBy.XPATH, "//*[@text='股票']")

    def goto_stock_tab(self):
        """切换到 tab 的【股票】"""
        # click 股票
        self.find_and_click(*self._MENU_STOCK)
        return self

    def get_price(self, stock_num):
        """找到 股票【阿里巴巴】的股票价格 price"""
        # 找到阿里巴巴所对应的股票价格
        current_price = self.find_and_gettext(AppiumBy.XPATH, f"//*[@text='{stock_num}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        return float(current_price)
