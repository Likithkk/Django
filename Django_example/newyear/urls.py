from django.urls import path

from . import views
# list of all allowable urls
urlpatterns=[
    path("",views.index,name="index")
]