import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from core.Constants import Constants
from core.Performance_Evaluation_core import Performance_Evaluation_core
from core.login_page import LoginPage
from core.performance_page import PerformancePage


@ddt
class Performance_Evaluation_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.PE_inst = Performance_Evaluation_core()
        cls.service = Service()
        cls.chrome_options = webdriver.ChromeOptions()
        cls.path = Constants.path
        # cls.chrome_options.add_argument('--headless')

    def setUp(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def tearDown(self):
        self.driver.quit()

    @data(*Performance_Evaluation_core().get_csv_data('../config/PE_users.csv'))
    @unpack
    def test_Performance_Evaluation(self, username, password, user_type):
        login_page = LoginPage(self.driver)
        performance_page = PerformancePage(self.driver)

        self.driver.get(self.path)
        login_page.log_in(username, password)

        login_success = performance_page.check_login_success(self.path, user_type)
        self.assertTrue(login_success, f'Login failed for user type: {user_type}')


if __name__ == '__main__':
    unittest.main()
