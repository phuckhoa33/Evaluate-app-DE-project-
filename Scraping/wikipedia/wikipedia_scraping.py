import requests
from bs4 import BeautifulSoup


def scraping(url: str):
    response = requests.get(url)
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find('div', attrs={'class': 'vector-header-container'})
    print(table)


def main():
    scraping('https://en.wikipedia.org/wiki/Epsom_riot')


if __name__ == "__main__":
    main()
