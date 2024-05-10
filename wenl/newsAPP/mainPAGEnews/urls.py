from django.urls import path

from . import views

app_name = "mainPAGEnews"
urlpatterns = [
    path("", views.mainPAGE.as_view(), name="home"),
    path("test", views.test.as_view(), name="test"),
]