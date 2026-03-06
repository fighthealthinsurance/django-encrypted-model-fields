from django.urls import path
from django.contrib import admin

from django_encrypted_filefield.constants import FETCH_URL_NAME

from .views import MyDetailView, MyFetchView, MyFormView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("detail/<int:pk>/", MyDetailView.as_view(), name="detail"),
    path("", MyFormView.as_view(), name="index"),
    # This URL has to exist somewhere with this pattern and this name.  The
    # view used is up to you.
    path("fetch/<path:path>", MyFetchView.as_view(), name=FETCH_URL_NAME),
]
