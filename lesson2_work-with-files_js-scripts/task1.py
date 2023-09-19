import math
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

driver = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def first_task(linkk: str) -> None:
    try:
        driver.get(linkk)
        a = int(driver.find_element(By.ID, "num1").text)
        b = int(driver.find_element(By.ID, "num2").text)
        sum = a+b
        print(sum)

        select = Select(driver.find_element(By.TAG_NAME, 'select'))
        select.select_by_visible_text(str(sum))
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    finally:
        time.sleep(15)
        driver.quit()

def second_task(link="youtube.com") -> None:
    try:
        driver.get(link)
        x = int(driver.find_element(By.ID, "input_value").text)
        y = calc(x)
        driver.find_element(By.ID, "answer").send_keys(str(y))
        button = driver.find_element(By.TAG_NAME, "button")
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        driver.find_element(By.ID, "robotCheckbox").click()
        driver.find_element(By.ID, "robotsRule").click()
        button.click()
    finally:
        time.sleep(5)
        driver.quit()

def third_task(link="youtube.com") -> None:
    try:
        driver.get(link)
        print(__file__)

        driver.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Ivan")
        driver.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Kolov")
        driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("Ivasdadf@fdsan.com")

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, "for_task3.txt")
        print(file_path)
        driver.find_element(By.ID, 'file').send_keys(file_path)
        driver.find_element(By.TAG_NAME, "button").click()

    finally:
        time.sleep(5)
        driver.quit()



third_task("http://suninjuly.github.io/file_input.html")

