import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x = driver.find_element(By.ID, "input_value").text
    print(x)
    y = calc(x)
    print(y)

    ans = driver.find_element(By.ID, "answer").send_keys(y)

    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(15)
    driver.quit()