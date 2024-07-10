import os
import requests

if __name__ == "__main__":
    output_dir = "ignores"
    response = requests.get(url = "http://example.com/")
    with open(os.path.join(output_dir, "website.html"), "wt") as fl:
        fl.write(response.text)
    if not response.ok:
        print(response.text)