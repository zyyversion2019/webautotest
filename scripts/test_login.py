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
        DriverUtils.close_driver()

    def test_login_error1(self):
        self.login_page.click_login_link()
        self.login_page.input_username()
        self.login_page.input_password()
        self.login_page.input_verify_code()
        self.login_page.click_login_btn()
        time.sleep(3)
        msg=self.login_page.get_msg()

        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.ID, "username").send_keys("18510000000")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.CSS_SELECTOR, ".login_bnt > a").click()
        time.sleep(3)
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-padding").text
        print(msg)
        assert "账号不存在!" == msg
    def test_login_error2(self):
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.ID, "username").send_keys("18510688904")
        self.driver.find_element(By.ID, "password").send_keys("223456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.CSS_SELECTOR, ".login_bnt > a").click()
        time.sleep(3)
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-padding").text
        print(msg)
        assert "密码错误!" == msg
