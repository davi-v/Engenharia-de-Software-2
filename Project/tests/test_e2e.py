import pytest
from selenium import webdriver

def test_first_case_selenium():

	options = webdriver.FirefoxOptions()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	
	driver.get("http://127.0.0.1:80")
	assert "Upload File" in driver.title

	driver.quit()