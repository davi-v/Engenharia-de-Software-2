import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path

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

@pytest.fixture
def image_setup(browser):
	browser.get("http://127.0.0.1:80")

	input_title = browser.find_element(By.NAME, 'title')
	input_title.clear()
	input_title.send_keys("Bob")
	
	input_desc = browser.find_element(By.NAME, 'desc')
	input_desc.clear()
	input_desc.send_keys("Foto de um gatinho")


	input_file = browser.find_element(By.NAME, 'file')
	curDir = Path(__file__).parent 
	file =  str(curDir) + '/files/cat.jpeg'
	input_file.send_keys(file)

	form_element = browser.find_element(By.TAG_NAME,'form')
	form_element.submit()

@pytest.fixture
def audio_setup(browser):
	browser.get("http://127.0.0.1:80")

	input_title = browser.find_element(By.NAME, 'title')
	input_title.clear()
	input_title.send_keys("Music")
	
	input_desc = browser.find_element(By.NAME, 'desc')
	input_desc.clear()
	input_desc.send_keys("Audio de teste")


	input_file = browser.find_element(By.NAME, 'file')
	curDir = Path(__file__).parent 
	file =  str(curDir) + '/files/teste.mp3'
	input_file.send_keys(file)

	form_element = browser.find_element(By.TAG_NAME,'form')
	form_element.submit()

def test_home_title(browser):
	browser.get("http://127.0.0.1:80")
	assert "Upload File" in browser.title

def test_upload_image(browser, image_setup):
	assert "http://127.0.0.1/uploads" in browser.current_url
	assert "Bob" in browser.title
	
	h1 = browser.find_element(By.TAG_NAME, 'h1')
	p = browser.find_element(By.TAG_NAME, 'p')

	assert 'Bob' == h1.text
	assert 'Foto de um gatinho' == p.text

def test_upload_audio(browser, audio_setup):
	assert "http://127.0.0.1/uploads" in browser.current_url
	assert "Music" in browser.title

	h1 = browser.find_element(By.TAG_NAME, 'h1')
	p = browser.find_element(By.TAG_NAME, 'p')

	assert 'Music' == h1.text
	assert 'Audio de teste' == p.text

def test_search_for_image(browser, image_setup):
	browser.get("http://127.0.0.1/search")

	input_title = browser.find_element(By.NAME, 'title')
	input_title.clear()
	input_title.send_keys("Bob")

	form_element = browser.find_element(By.TAG_NAME,'form')
	form_element.submit()

	h1 = browser.find_element(By.TAG_NAME, 'h1')
	assert 'Arquivos Encontrados' == h1.text

	table_content = []
	rows = browser.find_elements(By.XPATH,"//table/tbody/tr")
	
	for row in rows:
	    cols = row.find_elements(By.XPATH,"./*")
	    for col in cols:
	    	table_content.append(col.text)

	assert "Bob" in str(table_content)

def test_search_for_audio(browser, audio_setup):
	browser.get("http://127.0.0.1/search")

	input_title = browser.find_element(By.NAME, 'title')
	input_title.clear()
	input_title.send_keys("Music")

	form_element = browser.find_element(By.TAG_NAME,'form')
	form_element.submit()

	h1 = browser.find_element(By.TAG_NAME, 'h1')
	assert 'Arquivos Encontrados' == h1.text

	table_content = []
	rows = browser.find_elements(By.XPATH,"//table/tbody/tr")
	
	for row in rows:
	    cols = row.find_elements(By.XPATH,"./*")
	    for col in cols:
	    	table_content.append(col.text)

	assert "Music" in str(table_content)