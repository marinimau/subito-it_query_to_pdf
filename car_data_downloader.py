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

    def __init__(self, factory=None, model=None, version=None, fuel_type=None, year=None, km=None, insertion_link=None,
                 city=None):
        """
        Constructor
        :param factory: the factory name
        :param model: the model name
        :param version: the version of the car
        :param fuel_type: the fuel type
        :param year: the year
        :param km: the km of the car
        :param insertion_link: the link of the insertion
        :param city: the city of the insertion
        """
        self.factory = factory
        self.model = model
        self.version = version
        self.fuel_type = fuel_type
        self.year = year
        self.km = km
        self.insertion_link = insertion_link
        self.city = city


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
    car_history_items = get_class(item_soup, 'feature-list_feature__2QHiI', 'li')
    process_car_history_items(car_history_items)


def process_car_history_items(car_history_items):
    """
    Process the car history items and return a CarItem obj
    :param car_history_items: the soup of car history section
    :return: the car obj
    """
    for item in car_history_items:
        label = get_class(item, 'feature-list_label__kALYE', 'span')[0].text
        print(label)


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
