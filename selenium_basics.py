from IPython import embed
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    # Basic usage
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # embed() # uncomment to pause execution
    driver.close()

    # Connecting to an existing chrome instance
    # start chrome using the following command first
    # chrome.exe --remote-debugging-port=9222
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)
    embed()