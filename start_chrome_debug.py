from IPython import embed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=chrome_options)
embed()
