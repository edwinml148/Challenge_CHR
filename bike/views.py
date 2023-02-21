from rest_framework import status
from rest_framework.response import Response
from rest_typed_views import typed_api_view
from bike.services import data_injection_from_api


@typed_api_view(["POST"])
def data_injection() -> Response:
    count_rows = data_injection_from_api()
    message = f"created {count_rows} records in biker_extras and biker_stations table"
    if count_rows == 0:
        message = "There is no more update in the api"
    return Response({"status": message}, status.HTTP_200_OK)
