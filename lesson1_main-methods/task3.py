import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get(link)

    pict = driver.find_element(By.TAG_NAME, "img")
    x = pict.get_attribute("valuex")

    ans = calc(x)
    driver.find_element(By.ID, "answer").send_keys(ans)
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "[type='Submit']").click()

finally:
    time.sleep(15)
    driver.quit()
