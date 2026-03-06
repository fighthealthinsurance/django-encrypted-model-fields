from django.test import SimpleTestCase

from ..crypt import Cryptographer


class CryptographerTestCase(SimpleTestCase):

    def test_encryption(self):
        data = b"This is some data"
        self.assertNotEqual(Cryptographer.encrypted(data), data)

    def test_decryption(self):
        data = b"This is some data"
        self.assertEqual(
            Cryptographer.decrypted(Cryptographer.encrypted(data)), data
        )
