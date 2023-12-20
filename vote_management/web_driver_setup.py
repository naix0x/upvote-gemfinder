from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

def setup_webdriver():
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    
    geckodriver_path = "/bin/geckodriver"
    service = FirefoxService(geckodriver_path)

    return webdriver.Firefox(options=options, service=service)
