import requests
from bs4 import BeautifulSoup

# Wat zijn de demografische gegevens van de reviewers?
# Hoeveel reviewers raden het product aan?
# Wat zijn de meest voorkomende kenmerken van het product?

def generateSoup():
    url = 'https://www.bol.com/nl/nl/p/de-jongen-de-mol-de-vos-en-het-paard/9200000128095686/?promo=main_803_POPC_B3_product_0_&bltgh=m0R10Q-aPf-OK5J1ISlMyw.49_gYnngoQ1VrqwYEo3071Khg_0_1_2.3.ProductImage#product-reviews'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def getListOfString(soup):
    div = soup.find('div', {'class':'u-pl--xxs'})
    string_list = div.get_text().split(' ', 1)
    return string_list

def getNumOfReviews():
    review_string_list = getListOfString(generateSoup())[1].split(' ')
    reviews = review_string_list[0].removeprefix('(')
    print(reviews)

def getRating():
    rating = getListOfString(generateSoup())[0].removesuffix('/5')
    print(rating)

# Returns list with demographic info of every reviewer 
def getDemographics(soup):
    list_of_ul = soup.find_all('ul', {'class': 'review-metadata__list'})
    all_demos = []
    for ul in list_of_ul:
        list_of_li = list(ul.descendants)
        demos = list_of_li[2::3]
        all_demos.append(demos)
    return all_demos

# Prints list with age of every reviewer 
def getAges():
    ages = []
    for list in getDemographics(generateSoup()):
        age = list[1]
        ages.append(age)
    print(ages)

# Prints list with city of every reviewer
def getCities():
    cities = []
    for list in getDemographics(generateSoup()):
        city_string = list[2].get_text().lower()
        if city_string[0].isalpha():
            city = city_string.split(' ')[0]
            cities.append(city.lower())
    print(cities)

getNumOfReviews()
getRating()
getAges()
getCities()
