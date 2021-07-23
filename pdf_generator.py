#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#
import requests
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

    def add_images(self, photos):
        """
        add images to pdf
        :param photos: the photo urls
        """
        if len(photos) > 0:
            self.image(str(photos[0]), x=0, w=pdf_w/2 - 10, type='jpeg')
        if len(photos) > 0:
            self.image(str(photos[1]), x=pdf_w/2, w=pdf_w/2 - 10, type='jpeg')

    def save(self, title):
        """
        Save a pdf
        :param title: the title of the file
        :return:
        """
        self.output(str('outputs/' + title + '.pdf'), 'F')


