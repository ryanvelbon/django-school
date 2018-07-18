# Harry Percival book

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_foobar(self):
        # John visits homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention "VB Tuition"
        self.assertIn('VB Tuition', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
