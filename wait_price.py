import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


def track_element(element):
    browser.execute_script("arguments[0].setAttribute('style', 'background-color: rgb(222, 0, 0);')", element)


link = "http://suninjuly.github.io/explicit_wait2.html"


with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, '.card-body #book')

    # wait price
    WebDriverWait(browser, 12).until(e_c.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.card-title + #price'), '$100'))

    button.click()
    track_element(button)
    track_element(browser.find_element(By.CSS_SELECTOR, '.card-title + #price'))

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    track_element(x_element)
    test_number = x_element.text

    response = calc(test_number)

    input_number = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    track_element(input_number)
    input_number.send_keys(response)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    print(browser.switch_to.alert.text.split()[-1])

