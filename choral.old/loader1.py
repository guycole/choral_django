#
# Title: loader.py
# Description:
# Development Environment: OS X 10.10.5/Python 2.7.7
# Author: G.S. Cole (guycole at gmail dot com)
#
import os
import sys

import xmltodict

#class ManifestXmlParser:


class ManifestLoader:

    def execute(self, file_name):
        print('execute')

        if os.path.exists(file_name):
            print("file exists")
            with open(file_name) as fd:
                doc = xmltodict.parse(fd.read())

            print(doc)
        else:
            print("not exist")

print('start loader')

#
#
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = 'unknown'

    driver = ManifestLoader()
    driver.execute(file_name)

print('stop loader')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
