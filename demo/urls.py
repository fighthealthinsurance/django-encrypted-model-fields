from django.urls import path, re_path
from django.contrib import admin

from django_encrypted_filefield.constants import FETCH_URL_NAME

from .views import MyDetailView, MyFetchView, MyFormView


urlpatterns = [
    path(r"admin/", admin.site.urls),
    re_path(r"^detail/(?P<pk>\d+)$", MyDetailView.as_view(), name="detail"),
    path("", MyFormView.as_view(), name="index"),
    # This URL has to exist somewhere with this pattern and this name.  The
    # view used is up to you.
    re_path(r"^fetch/(?P<path>.+)", MyFetchView.as_view(), name=FETCH_URL_NAME)
]
