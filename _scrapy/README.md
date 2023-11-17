# Getting Started
- Create a Scrapy project. This section will use `sandbox` as the project.
  ```
  scrapy startproject sandbox
  ```
- Define a spider under sandbox/sandbox/spiders.
  - Name the spider by setting a class variable `name`. This section will use
    `basics` as the spider name.
  - List urls in method `start_requests`.
  - Define parsing logic in `parse`.
- Figure out parsing logic by using scrapy shell.
  - Start scrapy shell
    ```
    scrapy shell url
    ```
  - Try different CSS selectors.
    - Use development mode of your website to determine selectors of interest.
    - Refer to CSS Selectors Reference in Links and Resources.
    - basics_spider.py
- Run the spider. The spider must have a class attribute `name`.
  ```
  cd sandbox
  scrapy crawl basics
  ```

# Other Tools
- [Selector Gadget](https://selectorgadget.com/)

# Links and Resources
- [Installation Guide](https://docs.scrapy.org/en/latest/intro/install.html)
- [Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project)
- [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.php)