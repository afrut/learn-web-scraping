from IPython import embed
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    embed()
    driver.close()
