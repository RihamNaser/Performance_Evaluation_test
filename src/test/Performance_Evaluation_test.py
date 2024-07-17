import unittest
from ddt import *
from core.Performance_Evaluation_core import Performance_Evaluation_core
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from core.Constants import Constants


@ddt
class Performance_Evaluation_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.PE_inst = Performance_Evaluation_core()
        cls.service = Service()
        cls.chrome_options = webdriver.ChromeOptions()
        # cls.chrome_options.add_argument('--headless')

    def tearDown(self):
        self.driver.quit()

    @data(*(Performance_Evaluation_core().get_csv_data('../config/PE_users.csv')))
    @unpack
    def test_Performance_Evaluation(self, username, password, Type):
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.PE_inst.log_in(self.driver, username, password, Constants.path)
