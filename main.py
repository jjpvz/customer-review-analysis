import requests
from bs4 import BeautifulSoup



def generateSoup():
    url = 'https://www.bol.com/nl/nl/p/de-jongen-de-mol-de-vos-en-het-paard/9200000128095686/?promo=main_803_POPC_B3_product_0_&bltgh=m0R10Q-aPf-OK5J1ISlMyw.49_gYnngoQ1VrqwYEo3071Khg_0_1_2.3.ProductImage'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

