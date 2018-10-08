#
# Title: loader.py
# Description:
# Development Environment: OS X 10.10.5/Python 2.7.7
# Author: G.S. Cole (guycole at gmail dot com)
#
import sys

class ManifestLoader:

    def execute(self, file_name):
        print('execute')

        with open(file_name, 'rt') as in_file:
            buffer = in_file.readlines()

        print(buffer)


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
