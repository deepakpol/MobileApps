import unittest
from django.utils.text import slugify


class SlugifyUnicodeTransliterationTest(unittest.TestCase):
    def test_unicode_transliterated_to_ascii_by_default(self):
        """
        Test that Unicode characters are transliterated to ASCII by default.
        Given 'Café Déjà Vu' with accents and allow_unicode=False,
        when slugify is applied, then the result is 'cafe-deja-vu'.
        """
        # Test with default allow_unicode=False
        result = slugify('Café Déjà Vu')
        self.assertEqual(result, 'cafe-deja-vu')
        
        # Test with explicit allow_unicode=False
        result_explicit = slugify('Café Déjà Vu', allow_unicode=False)
        self.assertEqual(result_explicit, 'cafe-deja-vu')