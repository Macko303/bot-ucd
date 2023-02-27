import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome()#options=options)

try:
    driver.get("https://youcandance.tvp.pl/konkurs")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/div[2]")))
    driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/div[2]").click()

                                
    mazowieckie = driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[7]/div[1]")
    ActionChains(driver).move_to_element(mazowieckie).perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[1]")))
    driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[1]").click()


    okno = driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[21]")
    ActionChains(driver).move_to_element(okno).perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[17]/div/div[2]/span")))
    driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[17]/div/div[2]/span").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[18]/div/div[2]/span")))
    driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[18]/div/div[2]/span").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[19]/div/div[2]/span")))
    driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[2]/div/div[6]/div[2]/div/div[19]/div/div[2]/span").click()

    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[3]/div/div/div/button")))
    driver.find_element(By.XPATH, "/html/body/section[2]/div/section/section/section/section/div[4]/div/div/div[3]/div/div/div/button").click()
    try:
        inf = driver.find_element(By.XPAT, "/html/body/section[2]/div/section/section/section/section/div[3]/div/div/div/div/p").text
        print(inf)
    except:
        pass

    driver.quit()
except:
    driver.quit()
    

