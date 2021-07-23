#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

import urllib.request

from fpdf import FPDF

pdf_w = 270
pdf_h = 210


class PDF(FPDF):
    """
    Defining a custom pdf class
    """

    def __init__(self):
        """
        constructoor
        """
        super().__init__(orientation='L', format='A4')

    def custom_header(self, car):
        """
        Create the custom header
        :param car: the car obj
        :return:
        """
        # Select Arial bold 15
        self.set_font('Arial', 'B', 10)
        self.cell(pdf_w/5, 8, txt='Marca: ' + car.factory(), border=1)
        self.cell(pdf_w/5, 8, txt='Modello: ' + car.model(), border=1)
        self.cell(pdf_w/5, 8, txt='Versione: ' + car.version(), border=1)
        self.cell(pdf_w/5, 8, txt=car.km(), border=1)
        self.cell(pdf_w/5, 8, txt='Immatricolazione: ' + car.year(), border=1)
        # Line break
        self.ln(20)

    def add_images(self, photos, car_id):
        """
        add images to pdf
        :param photos: the photo urls
        :param car_id: the document id
        """
        if len(photos) > 0:
            urllib.request.urlretrieve(str(photos[0]), "photos/" + car_id + ".jpeg")
            self.image("photos/" + car_id + ".jpeg", x=20, h=pdf_h/1.5 - 10, type='jpeg')

    def save(self, title):
        """
        Save a pdf
        :param title: the title of the file
        :return:
        """
        self.output(str('outputs/' + title + '.pdf'), 'F')


