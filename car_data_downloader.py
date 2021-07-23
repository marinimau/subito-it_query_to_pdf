#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

import requests
import re

from bs4 import BeautifulSoup

from utils import get_class

class CarItem:
    """
    The subito.it research car item
    """

    def __init__(self, factory, model, version, fuel_type, year, km, photos):
        """
        Constructor
        :param factory: the factory name
        :param model: the model name
        :param version: the version of the car
        :param fuel_type: the fuel type
        :param year: the year
        :param km: the km of the car
        :param photos: an array containing the url of the photos
        """
        factory = factory
        model = model
        version = version
        fuel_type = fuel_type
        year = year
        km = km
        photos = photos


def make_request(url):
    """
    Make the request and return a soup obj
    :param url: the subito.it url
    :return: a bs4 obj
    """
    http_response = requests.get(url).text
    return BeautifulSoup(http_response, 'html.parser')


def download_data(url):
    """
    Download the data from a research url
    :param url: the subito.it research url
    :return:
    """
    soup = make_request(url)
    car_insertions = get_class(soup, 'items__item BigCard-module_card__1pCxB')
    for insertion in car_insertions:
        link = get_class(insertion, 'BigCard-module_link__3TIKt', tag_name='a')
        if link is not None and len(link) > 0:
            read_item_page(link[0]['href'])


def read_item_page(url):
    """
    Load item page and get car attributes and photo
    :param url:
    :return:
    """
    item_soup = make_request(url)
    print(item_soup)
    print('\n\n\n\n\n\n\n')


def find_km(insertion, car_obj):
    """
    Find the km of the current car
    :param insertion: the bs4 insertion obj
    :param car_obj: a CarItem instance
    :return:
    """
    try:
        price = insertion.find('p', class_=re.compile(r'price')).contents[0]
        # at the moment (20.5.2021) the price is under the 'p' tag with 'span' inside if shipping available
    except:
        price = "Unknown price"
    car_obj.price = price
