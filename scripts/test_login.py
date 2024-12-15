# author zyy
# time 2024/12/15 16:21
import time

from selenium.webdriver.common.by import By

from page.login_page import LoginPage
from utils.driver_utils import DriverUtils


class TestLogin:

    def setup_method(self):
        self.driver = DriverUtils.get_driver()
        self.login_page=LoginPage(self.driver)
        self.driver.get("http://192.168.10.139/Home/Index/index.html")

    def teardown_method(self):
        time.sleep(3)
        DriverUtils.close_driver()

    def test_login_error1(self):
        self.login_page.click_login_link()
        self.login_page.input_username("18510000000")
        self.login_page.input_password("123456")
        self.login_page.input_verify_code("8888")
        self.login_page.click_login_btn()
        time.sleep(3)
        assert "账号不存在!" == self.login_page.get_msg()

    def test_login_error2(self):
        self.login_page.click_login_link()
        self.login_page.input_username("18510688904")
        self.login_page.input_password("223456")
        self.login_page.input_verify_code("8888")
        self.login_page.click_login_btn()
        time.sleep(3)
        assert "密码错误!" == self.login_page.get_msg()
