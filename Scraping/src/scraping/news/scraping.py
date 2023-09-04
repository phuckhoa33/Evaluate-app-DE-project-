from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def scraping(url):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=url, options=options)
    products = []  # List to store name of the product
    prices = []  # List to store price of the product
    ratings = []  # List to store rating of the product
    driver.get('<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq')
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
        rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)

    df = pd.DataFrame(
        {'Product Name': products, 'Price': prices, 'Rating': ratings})
    df.to_csv('products.csv', index=False, encoding='utf-8')


def main():
    scraping("/usr/lib/chromium-browser/chromedriver")


if __name__ == '__main__':
    main()
