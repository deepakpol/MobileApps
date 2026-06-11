from django.test import SimpleTestCase
from django.utils.text import slugify


class SlugifyPunctuationTest(SimpleTestCase):
    def test_slugify_strips_disallowed_punctuation(self):
        """
        Test that disallowed punctuation is stripped.
        Given 'C++ & Python: A Guide!', when slugify is applied,
        then punctuation is removed and the result is 'c-python-a-guide'.
        """
        result = slugify('C++ & Python: A Guide!')
        self.assertEqual(result, 'c-python-a-guide')