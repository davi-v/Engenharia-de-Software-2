import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
	chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

	chrome_options = Options()
	options = [
	    "--headless",
	    "--disable-gpu",
	    "--window-size=1920,1200",
	    "--ignore-certificate-errors",
	    "--disable-extensions",
	    "--no-sandbox",
	    "--disable-dev-shm-usage"
	]
	for option in options:
	    chrome_options.add_argument(option)
	
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
	
	yield driver

	driver.quit()

def test_title_selenium(browser):

	browser.get("http://127.0.0.1:80")
	assert "Upload File" in browser.title