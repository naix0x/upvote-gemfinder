from selenium.webdriver.common.by import By
from selenium_recaptcha_solver import RecaptchaSolver

def solve_recaptcha(driver):
    solver = RecaptchaSolver(driver=driver)
    recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    return recaptcha_iframe
