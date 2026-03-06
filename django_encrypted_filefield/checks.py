from django.core.checks import Error, Warning as CheckWarning, register
from django.urls import NoReverseMatch, reverse

from .constants import FETCH_URL_NAME, PASSWORD, SALT


@register("deff-constants")
def constants_check(app_configs, **kwargs):  # pylint: disable=unused-argument

    check_messages = []

    message = (
        "{} must be defined in your environment for "
        "django-encrypted-filefield to work."
    )

    if not SALT:
        check_messages.append(CheckWarning(message.format("DEFF_SALT")))
    if not PASSWORD:
        check_messages.append(CheckWarning(message.format("DEFF_PASSWORD")))

    return check_messages


@register("deff-fetch-url")
def fetch_url_check(app_configs, **kwargs):  # pylint: disable=unused-argument

    if not FETCH_URL_NAME:
        return []  # We've got bigger problems

    try:
        reverse(FETCH_URL_NAME, kwargs={"path": "anything"})
    except NoReverseMatch:
        return [
            Error(
                "django-encrypted-filefield requires that you define a url for "
                "the fetching the files."
            )
        ]

    return []
