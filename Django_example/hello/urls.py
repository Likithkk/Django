from django.urls import path

from . import views
# list of all allowable urls
urlpatterns=[
    path("", views.index1 , name="index"),
    path("<str:name>", views.greet , name="greet"),
    path("likith", views.likith , name="likith")
]