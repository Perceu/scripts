import requests
from bs4 import BeautifulSoup

# content of test_sample.py
def title_site():
    response = requests.get('https://perceu.github.io/')
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string


def test_title_site():
    assert title_site() == 'Perceu Bertoletti'