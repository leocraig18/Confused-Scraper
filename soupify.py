from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from classes import Quote

def extract_quotes(html):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = []

    # assuming each tbody represents a quote
    for tbody in soup.find_all('tbody'):
        # Extract the company name from the "alt" attribute of the image and remove the word 'logo'
        company = tbody.find('img', {'class': 'brand-logo'})['alt'].replace(' logo', '')

        # Extract the price and convert it to a float
        price_text = tbody.find('b', {'class': 'price'}).get_text()
        price = float(price_text.replace('£', '').replace(',', ''))  # remove currency symbol and commas

        # Features are true if they have a tick, otherwise false
        features = tbody.find_all('div', {'class': 'result__feature__status'})
        features_status = [feature.find('span').get_text().strip() == 'Yes' for feature in features]

        # Ensure we have exactly 5 features, otherwise, we need to handle this (either by raising an error or other means)
        if len(features_status) != 5:
            raise ValueError("Unexpected number of features")

        # Create a new Quote object and add it to the list
        quote = Quote(company, price, *features_status)
        quotes.append(quote)

    return quotes