import unittest
from django.utils.text import slugify


class TestSlugifySpacesToHyphens(unittest.TestCase):
    def test_spaces_become_single_hyphens_and_text_lowercased(self):
        """
        Test that spaces become single hyphens and text is lowercased.
        Given 'Hello World Foo', when slugify is applied, 
        then the result is 'hello-world-foo'.
        """
        result = slugify('Hello World Foo')
        self.assertEqual(result, 'hello-world-foo')