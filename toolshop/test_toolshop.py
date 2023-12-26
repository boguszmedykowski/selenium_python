import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import random
import string


def generate_random_email():
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(10))
    random_email = random_name + "example.com"
    return random_email


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    # driver.quit()


def wait(driver, by, value):
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, value)))


class TestTest1():
    def test_register(self, driver):
        credentials = {
            'first_name': 'test_name',
            'last_name': 'test_lastname',
            'dob': '02022000',
            'address': 'testowa1',
            'postcode': '11-111',
            'city': 'testowo',
            'state': 'wilkopolska',
            'country': 'Poland',
            'phone': '700800900',
            'password': 'Test123#'
        }
        credentials['email'] = generate_random_email()

        driver.get("https://practicesoftwaretesting.com/#/")
        driver.set_window_size(1024, 1028)

        wait(driver, By.LINK_TEXT, "Sign in").click()
        wait(driver, By.CSS_SELECTOR, "a[data-test='register-link']").click()

        wait(driver, By.ID, "first_name").send_keys(credentials['first_name'])
        wait(driver, By.ID, "last_name").send_keys(credentials['last_name'])

        dob_input = wait(driver, By.ID, "dob")
        actions = ActionChains(driver)
        actions.click(dob_input).send_keys(credentials['dob']).perform()

        wait(driver, By.ID, "address").send_keys(credentials['address'])
        wait(driver, By.ID, "postcode").send_keys(credentials['postcode'])
        wait(driver, By.ID, "city").send_keys(credentials['city'])
        wait(driver, By.ID, "state").send_keys(credentials['state'])

        dropdown_element = wait(driver, By.ID, "country")
        select = Select(dropdown_element)
        select.select_by_visible_text(credentials['country'])

        wait(driver, By.ID, "phone").send_keys(credentials['phone'])
        wait(driver, By.ID, "email").send_keys(credentials['email'])
        wait(driver, By.ID, "password").send_keys(credentials['password'])
        wait(driver, By.CLASS_NAME, "btnSubmit").click()
        wait(driver, By.XPATH, "//*[contains(text(), 'Login')]")


if __name__ == "__main__":
    pytest.main()
