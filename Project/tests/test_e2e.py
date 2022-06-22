import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def test_first_case_selenium():

	options = FirefoxOptions()
	options.add_argument("--headless")
	driver = webdriver.Firefox()
	
	driver.get("http://127.0.0.1:80")
	assert "Upload File" in driver.title

	driver.quit()