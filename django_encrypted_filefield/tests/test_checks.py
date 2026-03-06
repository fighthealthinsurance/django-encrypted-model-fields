from unittest import mock

from django.core.checks import Error, Warning
from django.test import SimpleTestCase

from ..checks import constants_check, fetch_url_check


class ConstantsCheckTestCase(SimpleTestCase):
    def test_no_warnings_when_configured(self):
        """No warnings when SALT and PASSWORD are set."""
        result = constants_check(None)
        self.assertEqual(result, [])

    @mock.patch("django_encrypted_filefield.checks.SALT", b"")
    def test_warning_when_salt_missing(self):
        result = constants_check(None)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Warning)
        self.assertIn("DEFF_SALT", result[0].msg)

    @mock.patch("django_encrypted_filefield.checks.PASSWORD", b"")
    def test_warning_when_password_missing(self):
        result = constants_check(None)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Warning)
        self.assertIn("DEFF_PASSWORD", result[0].msg)

    @mock.patch("django_encrypted_filefield.checks.SALT", b"")
    @mock.patch("django_encrypted_filefield.checks.PASSWORD", b"")
    def test_two_warnings_when_both_missing(self):
        result = constants_check(None)
        self.assertEqual(len(result), 2)


class FetchUrlCheckTestCase(SimpleTestCase):
    def test_no_errors_when_url_exists(self):
        """No errors when FETCH_URL_NAME resolves."""
        result = fetch_url_check(None)
        self.assertEqual(result, [])

    @mock.patch(
        "django_encrypted_filefield.checks.FETCH_URL_NAME",
        "nonexistent-url-name",
    )
    def test_error_when_url_not_found(self):
        result = fetch_url_check(None)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Error)

    @mock.patch(
        "django_encrypted_filefield.checks.FETCH_URL_NAME", None
    )
    def test_no_error_when_fetch_url_name_not_set(self):
        result = fetch_url_check(None)
        self.assertEqual(result, [])
