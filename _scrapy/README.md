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
  - Run the spider and write results to a json file outputs/quotes.json. This
    overwrites any existing file.
    ```
    scrapy crawl quotes -O outputs/quotes.json
    ```
  - Run the spider and append results to a multi-line json file
  outputs/quotes.jsonl.
    ```
    scrapy crawl quotes -o outputs/quotes.jsonl
    ```

# Rotating User Agents
  - [Scrapy rotating user agents in spider](https://stackoverflow.com/questions/67664845/scrapy-rotating-user-agents-in-spider)
  - [fake-useragent](https://pypi.org/project/fake-useragent/)
  - [How can I use a random user agent whenever I send a request?](https://stackoverflow.com/questions/67401114/how-can-i-use-a-random-user-agent-whenever-i-send-a-request/67432447#67432447)
  - [Scrapy Fake User Agents: How to Manage User Agents When Scraping](https://scrapeops.io/python-scrapy-playbook/scrapy-managing-user-agents/#what-are-user-agents--why-do-we-need-to-manage-them)

# Proxies and Rotating IPs
  - Check IP currently being used by scrapy
    ```
    scrapy crawl checkip --logfile outputs/checkip.log
    ```
  - Links
    - [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies)

# Using Scrapoxy
  - [Get AWS EC2 Credentials](https://scrapoxy.readthedocs.io/en/master/standard/providers/awsec2/get_credentials/index.html)
  - [Create a Security Group](https://scrapoxy.readthedocs.io/en/master/standard/providers/awsec2/create_security_group/index.html)
  - [Copy the forward-proxy AMI to your region](https://scrapoxy.readthedocs.io/en/master/standard/providers/awsec2/copy_ami_to_region/index.html)
  - [Run scrapoxy without Docker](https://scrapoxy.readthedocs.io/en/master/quick_start/index.html#step-3b-run-scrapoxy-without-docker)
    - Install make
      ```
      sudo apt-get install build-essential
      ```
    - Install nodejs and npm
      ```
      sudo apt update
      sudo apt install nodejs npm
      ```
    - Install scrapoxy
      ```
      sudo npm install -g scrapoxy
      ```
    - Create a scrapoxy configuration
      ```
      scrapoxy init ~/scrapoxy_conf.json
      ```
    - Modify this file and configure with AWS EC2 info
    - Add an environment variable `SCRAPOXY_CONF_PATH` pointing to this file
    - Run scrapoxy
      ```
      scrapoxy start "${SCRAPOXY_CONF_PATH}" -d
      ```
  - Open scrapoxy GUI at [this localhost link](http://localhost:8889)
  - [Configure the scraper to use scrapoxy](https://scrapoxy.readthedocs.io/en/master/tutorials/python-scrapy/#edit-settings-of-the-scraper)
  - Create an environment variable `SCRAPOXY_PASSWORD` to store the password
    used to authenticate to scrapoxy
  - [Test scrapoxy](https://scrapoxy.readthedocs.io/en/master/quick_start/index.html#step-6-test-scrapoxy)
    ```
    scrapoxy test http://localhost:8888
    curl --proxy http://127.0.0.1:8888 http://api.ipify.org
    ```
  - Links
    - [scrapoxy](https://www.scrapoxy.io/)
    - [scrapoxy Documentation](https://scrapoxy.readthedocs.io/en/master/index.html)

  ## Dockerize scrapoxy
  - Build the image
    ```
    make build
    ```
  - Run the interactive container
    ```
    make run_interactive
    ```
  - Run the service container
    ```
    make run
    ```
  - Cleanup
    ```
    make clean_docker
    ```

# Other Tools
  - [Selector Gadget](https://selectorgadget.com/)

# Links and Resources
  - [Installation Guide](https://docs.scrapy.org/en/latest/intro/install.html)
  - [Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project)
  - [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.php)
  - [Avoid getting banned](https://docs.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned)