import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    # driver.quit()


class TestTest1():
    def test_test1(self, driver):
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        driver.set_window_size(945, 1028)
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").send_keys("dddd")
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys("dddd")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()


# Uruchomienie testów za pomocą Pytest
if __name__ == "__main__":
    pytest.main()
