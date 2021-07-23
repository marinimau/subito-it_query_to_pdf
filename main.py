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
        public = PDF()
        private = PDF()
        i = 0
        for car in car_list:
            public.add_page()
            private.add_page()
            public.custom_header(car)
            private.custom_header(car)
            public.add_images(car.photos(), str(i))
            private.add_images(car.photos(), str(i))
            private.custom_footer(car)
            i += 1
        public.save(slugify(url))
        private.save(slugify(url), is_private=True)


