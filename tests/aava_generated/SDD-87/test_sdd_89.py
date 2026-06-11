import unittest
from django.utils.text import slugify


class TestSlugifyPunctuationStripping(unittest.TestCase):
    def test_disallowed_punctuation_is_stripped(self):
        """
        Test that punctuation is removed when slugify is applied.
        Given 'C++ & Python: A Guide!', the result should be 'c-python-a-guide'.
        """
        input_string = 'C++ & Python: A Guide!'
        expected_output = 'c-python-a-guide'
        
        result = slugify(input_string)
        
        self.assertEqual(result, expected_output)