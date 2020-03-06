# coding: utf-8

import csv
from utils.fill_script import ScriptForFiller
from utils.browser import Browser
from utils.file_name import FileName

from assertion.expect import Assert


class Matcher(object):
    """ fill_query, match_query, value """

    @staticmethod
    def match(csv_file: str):
        browser = Browser()
        root = browser.document()
        csv_path = FileName.input(csv_file)

        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if row[0].startswith('//'):
                    next
                s = ScriptForFiller(row[1])
                if s.is_script():
                    s.run()
                    next
                query = row[1]
                value = row[2]

                e = root.query_selector_all(query)
                v = e.get_value()

                Assert.expect(v).equals_to(value, 'Element: ' + query)
