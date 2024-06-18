from django.urls import path
from .views import Formlist

urlpatterns = [
    path('',Formlist.as_view(),name='formlist'),
]
