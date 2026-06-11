from django.test import SimpleTestCase
from django.utils.text import slugify


class SlugifyUnicodeTransliterationTest(SimpleTestCase):
    def test_slugify_unicode_transliteration_to_ascii_default(self):
        """
        Test that Unicode characters are transliterated to ASCII by default.
        Given 'Café Déjà Vu' with accents and allow_unicode=False (default),
        when slugify is applied, then the result is 'cafe-deja-vu'.
        """
        result = slugify("Café Déjà Vu", allow_unicode=False)
        self.assertEqual(result, "cafe-deja-vu")
    
    def test_slugify_unicode_transliteration_to_ascii_explicit(self):
        """
        Test that Unicode characters are transliterated to ASCII when
        allow_unicode is explicitly set to False.
        """
        result = slugify("Café Déjà Vu", allow_unicode=False)
        self.assertEqual(result, "cafe-deja-vu")