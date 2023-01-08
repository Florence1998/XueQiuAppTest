from appium.webdriver.common.appiumby import AppiumBy

black_list = [(AppiumBy.ID, "com.xueqiu.android:id/iv_close")]


# fun相当于find方法
def black_wrapper(fun):
    def run(*args, **kwargs):
        from xueqiu.base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            tmp_name = "tmp.png"
            basepage.screenshot(tmp_name)
            print("未找到元素，处理异常")
            for black in black_list:
                # 查找黑名单中的每一个元素
                eles = basepage.driver.find_elements(*black)
                if len(eles) > 0:
                    # 点掉弹框
                    eles[0].click()
                    # 继续查找元素
                    return fun(*args, **kwargs)
                raise e

    return run
