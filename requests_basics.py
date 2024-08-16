import os

import requests
from IPython import embed


def write_response(response: requests.Response):
    with open(os.path.join("ignores", "response.html"), "wt") as fl:
        fl.write(response.text)


if __name__ == "__main__":
    output_dir = "ignores"

    # Make a get request to a website
    response = requests.get(url="http://example.com/")
    write_response(response)
    if not response.ok:
        print(response.text)
