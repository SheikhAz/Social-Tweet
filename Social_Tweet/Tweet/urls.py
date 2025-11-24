from operator import index
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index ,name='index' ),
]
