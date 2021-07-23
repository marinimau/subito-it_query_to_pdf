#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

import requests

from bs4 import BeautifulSoup


class CarItem:
    """
    The subito.it research car item
    """

    def __init__(self, factory="", model="", version="", fuel_type="", year="", km="", insertion_link="",
                 city="", photos=""):
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
        :param photos: the photo url list
        """
        self._factory = factory
        self._model = model
        self._version = version
        self._fuel_type = fuel_type
        self._year = year
        self._km = km
        self._insertion_link = insertion_link
        self._city = city
        self._photos = photos

    def factory(self):
        """
        get factory
        :return: the factory value
        """
        return self._factory

    def model(self):
        """
        get model
        :return: the model value
        """
        return self._model

    def version(self):
        """
        get version
        :return: the version value
        """
        return self._version

    def fuel(self):
        """
        get fuel type
        :return: the fuel type value
        """
        return self._fuel_type

    def year(self):
        """
        get year
        :return: the year value
        """
        return self._year

    def km(self):
        """
        get km
        :return: the km value
        """
        return self._km

    def link(self):
        """
        get link
        :return: the link value
        """
        return self._insertion_link

    def city(self):
        """
        get city
        :return: the city value
        """
        return self._city

    def photos(self):
        """
        get photos
        :return: photos value
        """
        return self._photos

    def __str__(self):
        """
        to string method
        :return:
        """
        return str(self._insertion_link).replace(':', '').replace('/', '-').replace('.', '_')


def make_request(url):
    """
    Make the request and return a soup obj
    :param url: the subito.it url
    :return: a bs4 obj
    """
    http_response = requests.get(url).text
    return BeautifulSoup(http_response, 'html.parser')


def get_class(soup, class_css, tag_name='div'):
    """
    Get divs with the given class
    :param soup: the html soup
    :param class_css: the class name
    :param tag_name: the markup tag, default is div
    :return the list of divs with the given class
    """
    return soup.find_all(tag_name, class_=str(class_css))


def download_data(url):
    """
    Download the data from a research url
    :param url: the subito.it research url
    :return: a list that contains a car object for each car
    """
    soup = make_request(url)
    car_list = []
    car_insertions = get_class(soup, 'items__item BigCard-module_card__1pCxB')
    for insertion in car_insertions:
        link = get_class(insertion, 'BigCard-module_link__3TIKt', tag_name='a')
        if link is not None and len(link) > 0:
            car_list.append(read_item_page(link[0]['href']))
    return car_list


def read_item_page(url):
    """
    Load item page and get car attributes and photo
    :param url:
    :return: the car obj
    """
    item_soup = make_request(url)
    car_history_items = get_class(item_soup, 'feature-list_feature__2QHiI', 'li')
    city = get_class(item_soup, 'AdInfo_ad-info__location__text__1kXDa', 'span')[0].text
    photos = [photo['src'] for photo in get_class(item_soup, 'CarouselCell_image__dW-gN', 'img')]
    car_instance = CarItem(insertion_link=url, city=city, photos=photos)
    process_car_history_items(car_history_items, car_instance)
    return car_instance


def process_car_history_items(car_history_items, car_instance):
    """
    Process the car history items and return a CarItem obj
    :param car_history_items: the soup of car history section
    :param car_instance: the car instance
    """
    for item in car_history_items:
        label = get_class(item, 'feature-list_label__kALYE', 'span')[0].text
        value = get_class(item, 'feature-list_value__2nzDw', 'span')[0].text
        evaluate_item(label, value, car_instance)


def evaluate_item(label, value, car_instance):
    """
    Evaluate the item and insert the value in the correct field of te car isntance
    :param label: the item label
    :param value: the item value
    :param car_instance: the car obj
    :return:
    """
    if label == 'Marca':
        car_instance._factory = value
    elif label == 'Modello':
        car_instance._model = value
    elif label == 'Versione':
        car_instance._version = value
    elif label == 'Carburante':
        car_instance._fuel_type = value
    elif label == 'Immatricolazione':
        car_instance._year = value
    elif label == 'Km':
        car_instance._km = value
