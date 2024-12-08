from bs4 import BeautifulSoup
import requests

site_link ="https://appbrewery.github.io/Zillow-Clone/"

class SoupManager:
    def __init__(self):
        response = requests.get(site_link)

        self.soup = BeautifulSoup(response.text, "html.parser")

    def turn_add_list(self):
        all_adress = [address.getText().lstrip().replace("\n", "").strip() for address in
                      self.soup.find_all("address", {'data-test': 'property-card-addr'})]
        return all_adress

    def turn_price_list(self):
        all_price = [price.getText() for price in
                     self.soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
        return all_price

    def turn_link_list(self):
        all_link = [link['href'] for link in self.soup.find_all(class_="property-card-link", href=True)]
        return all_link
