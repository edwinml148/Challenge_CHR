from django.urls import path
from evaluacion_ambiental.views import data_scraper 

urlpatterns = [
    path('create_table', data_scraper),
]
