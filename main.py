#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

from slugify import slugify

from car_data_downloader import download_data
from conf import research_urls
from pdf_generator import PDF


if __name__ == '__main__':
    for url in research_urls:
        car_list = download_data(url)
        p = PDF()
        for car in car_list:
            p.add_page()
            p.custom_header(car)
            p.add_images(car.photos())

        p.save(slugify(url))


