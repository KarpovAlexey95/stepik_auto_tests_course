from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC#The owls  are not what they seem! OvO
import time
import math

def answer():
    return str(math.log(int(time.time())))
links = ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize("link", links)
def test_guest_should_see_login_link(browser, link):
    browser.implicitly_wait(10)
    browser.get(link)

    #логинимся
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    button.click()
    login_input = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    login_input.send_keys("***********")
    password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password_input.send_keys("********")
    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()

    time.sleep(5)
    #ввод ответа
    browser.find_element(By.CSS_SELECTOR, "textarea.textarea").send_keys(answer())
    time.sleep(5)
    button = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    print(button)
    button.click()
    button.click()
    button.click()
    print("4")
    time.sleep(5)
    mes = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ember-view p"))
    )
    print("5")
    text = mes.text
    assert "Correct!" == text, f"Найдено загадочное сообщение инопланетян: {text}"

