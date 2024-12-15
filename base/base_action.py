# author zyy
# time 2024/12/15 23:28
class BaseAction:

    def __init__(self,driver):
        self.driver=driver

    def find_ele(self,fixture):
        return self.driver.find_element(*fixture)