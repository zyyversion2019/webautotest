# author zyy
# time 2024/12/15 22:39
from selenium.webdriver.common.by import By


class LoginPage:

    login_link_btn=By.LINK_TEXT, "登录"
    username_input=By.ID, "username"
    password_input=By.ID, "password"
    verify_code_input=By.ID, "verify_code"
    login_btn=By.CSS_SELECTOR, ".login_bnt > a"
    msg= By.CSS_SELECTOR, ".layui-layer-padding"


    def __init__(self,driver):
        self.driver=driver

    def find_ele(self,fixture):
        return self.driver.find_element(*fixture)

    def click_login_link(self):
        return self.find_ele(self.login_link_btn).click()

    def input_username(self,username):
        return  self.find_ele(self.username_input).send_keys(username)

    def input_password(self,password):
        return  self.find_ele(self.password_input).send_keys(password)

    def input_verify_code(self, verify_code):
        return  self.find_ele(self.verify_code_input).send_keys(verify_code)

    def click_login_btn(self):
        return  self.find_ele(self.login_btn).click()

    def get_msg(self):
        return self.find_ele(self.msg).text