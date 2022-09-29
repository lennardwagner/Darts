from django.urls import path

from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("test/", views.test2, name="test2"),
    path("1/", views.test_site, name="test-site"),
]
# rs