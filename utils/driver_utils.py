# author zyy
# time 2024/12/15 17:02
from selenium import webdriver


class DriverUtils:

    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(3)
            # cls.driver.get("http://192.168.10.139/Home/Index/index.html")
        return cls.__driver

    @classmethod
    def close_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver.close()

