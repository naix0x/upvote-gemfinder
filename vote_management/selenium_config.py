from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver  # Add this import statement

def configure_selenium(driver):
    test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
    
    capabilities = DesiredCapabilities.FIREFOX
    capabilities['moz:firefoxOptions'] = {
        'args': ['--headless', f'--user-agent={test_ua}']
    }
    
    driver = webdriver.Firefox(capabilities=capabilities)
