# Requests Module in Python

import requests
from bs4 import BeautifulSoup

"""
response = requests.get("https://google.com")
print(response.text)
"""

"""
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'udoy',
    "body": 'bhai',
    "userId": 12
}

headers = {
    'Content-type': 'application/json; charset=UTF-8'
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
"""


url = "https://www.codewithharry.com/blogpost/streamlining-quality-control/"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)
