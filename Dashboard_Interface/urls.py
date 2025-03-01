from django.urls import path
from .views import db_status_view

urlpatterns =[
    path('',db_status_view,name="name"),
]