from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://trustme.kz/contract/")
submit_button = browser.find_element(By.NAME, "login")
submit_button.click()
time.sleep(5)
# сделал паузы в пять секунд для наглядности, в целом можно убрать
phone = browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/input")
phone.send_keys("7021234567")
time.sleep(5)
password = browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div[2]/div/div[2]/div[2]/input")
password.send_keys("1234567")
time.sleep(5)
login_button = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div/div[4]/a[2]")
login_button.click()
time.sleep(5)
driver.quit()
