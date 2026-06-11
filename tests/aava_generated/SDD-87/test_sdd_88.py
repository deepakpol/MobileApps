from django.test import SimpleTestCase
from django.utils.text import slugify


class SlugifySpacesToHyphensTest(SimpleTestCase):
    def test_spaces_become_single_hyphens_and_text_is_lowercased(self):
        """
        Given 'Hello World Foo', when slugify is applied,
        then the result is 'hello-world-foo'.
        """
        result = slugify('Hello World Foo')
        self.assertEqual(result, 'hello-world-foo')