#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

from car_data_downloader import download_data
from conf import research_urls

if __name__ == '__main__':
    for url in research_urls:
        download_data(url)


