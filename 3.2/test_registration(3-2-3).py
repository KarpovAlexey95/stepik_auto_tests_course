from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def test_case(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your first name\"]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your last name\"]")
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your email\"]")
    input3.send_keys("Ivan")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    return welcome_text_elt.text


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(test_case("http://suninjuly.github.io/registration1.html"), \
                         "Congratulations! You have successfully registered!", \
                         "Should be absolute value of a number")

    def test_registration2(self):
        self.assertEqual(test_case("http://suninjuly.github.io/registration2.html"), \
                         "Congratulations! You have successfully registered!", \
                         "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
