# coding: utf-8

import csv
from utils.fill_script import ScriptForFiller
from utils.browser import Browser
from utils.file_name import FileName


class Filler(object):
    """ fill_query, match_query, value """

    @staticmethod
    def fill(csv_file: str):
        browser = Browser()
        root = browser.document()
        csv_path = FileName.input(csv_file)

        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if row[0].startswith('//'):
                    next
                s = ScriptForFiller(row[0])
                if s.is_script():
                    s.run()
                    next
                query = row[0]
                value = row[2]

                e = root.query_selector_all(query)
                e.set_value(value)
