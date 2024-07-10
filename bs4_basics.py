import requests

from bs4 import BeautifulSoup

if __name__ == "__main__":
    print("requesting")
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    # Create BeautifulSoup object by parsing html of page contents
    soup = BeautifulSoup(page.content, "html.parser")

    # Find object by id
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")

    for job_element in job_elements:
        # Find h2 tag with class title
        title_element = job_element.find("h2", class_="title")

        # Get text content of html tag
        title_text = title_element.text

    # Find all h2 tags with matching text content
    python_jobs = results.find_all("h2", string="Python")

    # Find all h2 tags matching a specific criteria specified by a lambda
    # function
    python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

    # Find great grandparent of every tag.
    parents = [x.parent.parent.parent for x in python_jobs]

    # Find all hyperlink tags and retrieve url (href attribute) for 2nd tag
    hls = list(parents[0].find_all("a"))
    url = hls[1]["href"]
