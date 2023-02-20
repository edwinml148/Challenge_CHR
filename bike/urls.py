from django.urls import path
from bike.views import data_injection

urlpatterns = [
    path("create_table", data_injection),
]
