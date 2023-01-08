import logging
import os
import traceback

import allure
from appium.webdriver.common.appiumby import AppiumBy

black_list = [(AppiumBy.ID, "com.xueqiu.android:id/iv_close")]


# fun相当于find方法
def black_wrapper(fun):
    def run(*args, **kwargs):
        from xueqiu.base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            logging.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except Exception as e:
            logging.warning("未找到元素，处理异常")
            # 以当前时间命名的截图
            curtime = basepage.get_time()
            tmp_name = curtime + ".png"
            # 当前black_handle.py所在的路径
            logging.info("当前保存图片的路径>>>" + os.path.dirname(__file__))
            # 找到images路肩，拼接图片名称
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", tmp_name)
            basepage.screenshot(tmp_path)
            allure.attach.file(tmp_path, name="查找截图", attachment_type=allure.attachment_type.PNG)
            for black in black_list:
                logging.info(f"处理黑名单：{black}")
                # 查找黑名单中的每一个元素
                eles = basepage.driver.find_elements(*black)
                if len(eles) > 0:
                    logging.info("点击黑名单弹框")
                    # 点掉弹框
                    eles[0].click()
                    # 继续查找元素
                    return fun(*args, **kwargs)
            logging.error(f"遍历黑名单，仍未找到元素，异常信息====>{e}")
            logging.error(f"traceback.format_exc()====>{traceback.format_exc()}")
            raise e

    return run
