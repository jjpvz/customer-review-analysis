import requests
from bs4 import BeautifulSoup
from collections import Counter

# TODO:
# 1. gemiddelde leeftijd van reviewers -- done
# 2. welke leeftijdsgroep geeft de hoogste rating
# 3. welke stad komt het meest voor -- done
# 4. hoeveel reviewers raden het product aan?
# 5. wat zijn de meest voorkomende kenmerken van het product?

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
# getNumOfReviews()

def getRating():
    rating = getListOfString(generateSoup())[0].removesuffix('/5')
    print(rating)
# getRating()

# Returns list with demographic info of every reviewer 
def getDemographics(soup):
    list_of_ul = soup.find_all('ul', {'class': 'review-metadata__list'})
    all_demos = []
    for ul in list_of_ul:
        list_of_li = list(ul.descendants)
        demos = list_of_li[2::3]
        all_demos.append(demos)
    return all_demos

# Returns list with age group of every reviewer 
def getAgeGroups():
    ages = []
    for list in getDemographics(generateSoup()):
        age = list[1]
        ages.append(age.get_text())
    # print(ages) 
    return ages
# getAgeGroups()

# Prints list with age group of every reviewer 
def generateAge():
    average_ages = []
    for age_group in getAgeGroups():
        average_age = age_group[0:2]
        average_ages.append(int(average_age) + 5)
    # print(average_ages)     
    return average_ages
# generateAge()

# Prints list with city of every reviewer
def getCities():
    cities = []
    for list in getDemographics(generateSoup()):
        city_string = list[2].get_text().lower()
        if city_string[0].isalpha():
            city = city_string.split(' ')[0]
            cities.append(city)      
    # print(cities)
    return cities

def getMostCommonCity():
    dictionary = dict(Counter(getCities()))
    max_key = max(dictionary, key = dictionary.get)
    print(max_key)
getMostCommonCity()

# Prints average age of all reviewers by dividing sum of all values in list by sum of all products of key multiplied by value
def getAverageAge():
    d = dict(Counter(generateAge()))
    reviewers = []
    x = []
    for key in d:
        reviewers.append(d[key])
        average_age_of_group = key * d[key]
        x.append(average_age_of_group)
    average_age = sum(x) // sum(reviewers)
    print(average_age)
# getAverageAge()
