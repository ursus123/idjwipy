# Importing necessary libraries
import os, unittest, sys
from idjwi.functions import open_data
sys.path.append(os.path.join(os.path.dirname(__file__),'idjwi'))


class open_dataTestCase(unittest.TestCase):

	def setUp(self):
		self.functions = open_data.csv_excel('ok.csv')


	def check_link(self, file_source):

		file_name, file_extension = os.path.splitext(file_source)
		self.assertEqual(file_extension,'csv')
		self.assertEqual(file_extension,'xlsx')

if __name__ == '__main__':
	unittest.main()


