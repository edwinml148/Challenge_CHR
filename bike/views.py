from django.shortcuts import render
import requests
from bike.lib.constans import API_BIKE_SANTIAGO
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_typed_views import Body, typed_api_view
from bike.services import data_injection_from_api
from rest_framework.response import Response

@typed_api_view(['PUT'])
def data_injection():
    count_rows = data_injection_from_api()
    message = f'created {count_rows} records in biker_extras and biker_stations table'
    if count_rows == 0:
        message = 'There is no more update in the api'
    return Response({'status': message}, status.HTTP_200_OK)
