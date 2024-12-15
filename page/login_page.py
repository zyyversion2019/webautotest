# author zyy
# time 2024/12/15 22:39
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    def click_login_link(self):
        return self.driver.find_element(By.LINK_TEXT, "登录").click()

    def input_username(self,username):
        return self.driver.find_element(By.ID, "username").send_keys(username)

    def input_password(self,password):
        return self.driver.find_element(By.ID, "password").send_keys(password)

    def input_verify_code(self, verify_code):
        return self.driver.find_element(By.ID, "verify_code").send_keys(verify_code)

    def click_login_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".login_bnt > a").click()

    def get_msg(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-padding").text
        return msg