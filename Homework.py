from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import string
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.select import Select

# browser = webdriver.Chrome
link = "http://suninjuly.github.io/find_link_text"
link2 = "http://suninjuly.github.io/find_xpath_form"
link3 = "http://suninjuly.github.io/selects1.html"
link4 = "http://suninjuly.github.io/selects2.html"
link5 = "http://suninjuly.github.io/execute_script.html"


def test_fill_form():
    browser = webdriver.Chrome()
    browser.get(link)
    a = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link1 = browser.find_element(By.LINK_TEXT, a)
    link1.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)
    browser.quit()


def test_huge_form():
    browser = webdriver.Chrome()
    letters = string.ascii_letters
    answer = ''.join(random.choice(letters) for _ in range(7))
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)
    browser.quit()


def test_xpath_form():
    browser = webdriver.Chrome()
    browser.get(link2)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "// button[text() = 'Submit']")
    button.click()
    time.sleep(10)
    browser.quit()


def test_another_registration():
    link3 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link3)
    answer1 = "abcde"
    obligatory_fields = browser.find_elements(By.CSS_SELECTOR, "input:required")
    for field in obligatory_fields:
        field.send_keys(answer1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)
    browser.quit()


def test_another_registration_extra():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
    input1.send_keys("Kathryn")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
    input2.send_keys("Janeway")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
    input3.send_keys("admiral.janeway@starfleet.org")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)
    browser.quit()


def test_robots_rule():
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys((y))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(20)
    browser.quit()


def test_find_treasure():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys((y))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(20)
    browser.quit()


def test_calculate_and_click():
    browser = webdriver.Chrome()
    browser.get(link4)
    num1 = browser.find_element(By.ID, "num1")
    a = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    b = int(num2.text)
    sum = a + b
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum))
    submit_btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_btn.click()
    time.sleep(20)
    browser.quit()


def test_close_footer():
    browser = webdriver.Chrome()
    browser.get(link5)
    num = browser.find_element(By.ID, "input_value")
    x = int(num.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(20)
    browser.quit()


def test_file_upload():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Kathryn")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Janeway")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("admiral.janeway@starfleet.org")
    browser.find_element(By.ID, "file").send_keys("C:/Users/Zoe/PycharmProjects/pythonProject1/stepik.txt")
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(20)
    browser.quit()


def test_accept_alert():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    # confirm = browser.switch_to.alert
    # confirm.accept()
    browser.switch_to.alert.accept()
    num = browser.find_element(By.ID, "input_value")
    x = int(num.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)
    browser.quit()


def test_redirect_accept():
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    driver.find_element(By.CLASS_NAME, 'trollface').click()
    driver.switch_to.window(driver.window_handles[1])
    num = driver.find_element(By.ID, "input_value")
    x = int(num.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)
    driver.quit()


def test_waits_book():
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    driver.find_element(By.ID, "book").click()
    num = driver.find_element(By.ID, "input_value")
    x = int(num.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.ID, "solve").click()
    time.sleep(15)
    driver.quit()

