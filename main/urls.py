from django.urls import path
from . import views

urlpatterns = [
    path("", views.test_site, name="test-site"),
    path("1/", views.test, name="test"),
]


# rs