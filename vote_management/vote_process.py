from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_vote(driver):
    btn_selector = '#singlevote'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, btn_selector)))
    btn = driver.find_element(By.CSS_SELECTOR, btn_selector)
    btn.click()
