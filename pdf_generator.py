#
#   subito-it_query_to_pdf copyright © 2021 - all rights reserved
#   Created at: 23/07/21
#   By: mauromarini
#   License: MIT
#   Repository: https://github.com/marinimau/subito-it_query_to_pdf
#   Credits: @marinimau (https://github.com/marinimau)
#

from fpdf import FPDF

pdf_w = 210
pdf_h = 297


class PDF(FPDF):
    """
    Defining a custom pdf class
    """

    def __init__(self):
        """
        constructoor
        """
        super().__init__(orientation='L', format='A4')

    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    def save(self, title):
        """
        Save a pdf
        :param title: the title of the file
        :return:
        """
        self.output(str('outputs/' + title + '.pdf'), 'F')


