from selenium.webdriver.common.by import By


class PerformancePage:
    def __init__(self, driver):
        self.driver = driver

    def check_login_success(self, path, user_type):
        current_url = self.driver.current_url
        return True if current_url == path + user_type else False
