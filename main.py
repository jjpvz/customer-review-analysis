import requests
from bs4 import BeautifulSoup



def generateSoup():
    url = 'https://www.bol.com/nl/nl/p/de-jongen-de-mol-de-vos-en-het-paard/9200000128095686/?promo=main_803_POPC_B3_product_0_&bltgh=m0R10Q-aPf-OK5J1ISlMyw.49_gYnngoQ1VrqwYEo3071Khg_0_1_2.3.ProductImage'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def getListOfString(soup):
    div = soup.find('div', {'class':'u-pl--xxs'})
    string_list = div.get_text().split(' ', 1)
    return string_list

def getNumOfReviews():
    review_string_list = getListOfString(generateSoup())[1].split(' ')
    #review_string_list = string_list[1].split(' ')
    reviews = review_string_list[0].removeprefix('(')
    print(reviews)

def getRating():
    rating = getListOfString(generateSoup())[0].removesuffix('/5')
    print(rating)

getNumOfReviews()
getRating()

# Wat zijn de demografische gegevens van de reviewers?
# Hoeveel reviewers raden het product aan?
# Wat zijn de meest voorkomende kenmerken van het product?
