from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from classes import Quote

def extract_quotes(html):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = []

    # Iterate over each parent <div class="result-container">
    for result_container in soup.find_all('div', {'class': 'result-container'}):

        # Check for the presence of the "Black box policy" text
        black_box_policy = bool(result_container.find(
            'b', string='Black box policy - '))

        # Find the tbody within the result_container
        tbody = result_container.find('tbody')

        # Continue extracting other details as before
        company = tbody.find(
            'img', {'class': 'brand-logo'})['alt'].replace(' logo', '')
        price_text = tbody.find('b', {'class': 'price'}).get_text()
        price = float(price_text.replace('£', '').replace(',', ''))

        features = tbody.find_all('div', {'class': 'result__feature__status'})
        features_status = [feature.find('span').get_text(
        ).strip() == 'Yes' for feature in features]
        if len(features_status) != 5:
            raise ValueError("Unexpected number of features")

        quote = Quote(company, price, *features_status, black_box_policy)
        quotes.append(quote)

    return quotes