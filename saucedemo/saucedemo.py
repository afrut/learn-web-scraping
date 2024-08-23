import os
from urllib.parse import urlparse, urlunsplit

from bs4 import BeautifulSoup
from IPython import embed
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def login(driver) -> None:
    try:
        username = driver.find_element(by=By.CSS_SELECTOR, value="input#user-name")
        username.clear()
        username.send_keys(os.environ["SAUCEDEMO_USERNAME"])
        password = driver.find_element(by=By.CSS_SELECTOR, value="input#password")
        password.clear()
        password.send_keys(os.environ["SAUCEDEMO_PASSWORD"])
        driver.find_element(by=By.CSS_SELECTOR, value="input#login-button").click()
    except NoSuchElementException:
        print("Already logged in.")
        return


if __name__ == "__main__":
    base_url = "https://www.saucedemo.com/"
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)

    # Wait 5 seconds before deciding that any enements cannot be found
    driver.implicitly_wait(5)

    if not (driver.current_url.startswith(base_url)):
        driver.get(base_url)
    login(driver)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find a div whose class is inventory_list
    inventory_list = soup.find("div", {"class": "inventory_list"})

    # Print prettified html
    print(inventory_list.prettify())

    # Loop through children
    items = []
    for item in inventory_list.children:
        name = item.find("div", {"class": "inventory_item_name"}).text
        description = item.find("div", {"class": "inventory_item_desc"}).text

        # Subsequent finds
        price = (
            item.find("div", {"class": "pricebar"})
            .find("div", {"class": "inventory_item_price"})
            .text.replace("$", "")
        )
        price = float(price)

        items.append({"name": name, "description": description, "price": price})

    for item in items:
        print(item)
