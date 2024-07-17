from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


class Performance_Evaluation_core:

    @staticmethod
    def get_csv_data(csv_path):
        rows = []
        csv_data = open(str(csv_path), "r", encoding="utf8")
        content = csv.reader(csv_data)
        next(content, None)
        for row in content:
            rows.append(row)
        return rows

    @staticmethod
    def log_in(driver, user_name, password, path):
        driver.set_window_size(1920, 1080)
        driver.get(path)

        WebDriverWait(driver, 700).until(
            EC.presence_of_element_located((By.ID, "email"))).send_keys(user_name)
        WebDriverWait(driver, 700).until(
            EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        WebDriverWait(driver, 700).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="myform"]/button'))).click()
