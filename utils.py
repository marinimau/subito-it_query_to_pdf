#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

def get_class(soup, class_css, tag_name='div'):
    """
    Get divs with the given class
    :param soup: the html soup
    :param class_css: the class name
    :param tag_name: the markup tag, default is div
    :return the list of divs with the given class
    """
    return soup.find_all(type, class_=str(class_css))
