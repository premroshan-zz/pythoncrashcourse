import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for namefunction.py"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_middle_last_name(self):
        """Test if names with middle name works"""
        formatted_name = get_formatted_name('prem', 'nair','roshan')
        self.assertEqual(formatted_name,'Prem Roshan Nair')

if __name__ == '__main__':
    unittest.main()