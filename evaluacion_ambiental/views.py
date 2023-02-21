from rest_framework import status
from rest_framework.response import Response
from rest_typed_views import Body, typed_api_view
from evaluacion_ambiental.services import data_injection_from_scraper, numbers_page_from_homepage


@typed_api_view(['POST'])
def data_scraper(
    homepage: int = Body(source='homepage', default=None),
    final_page: int = Body(source='final_page', default=None),
) -> Response:
    pages_max = numbers_page_from_homepage()
    if homepage >= final_page:
        return Response(
            {"error": "final_page debe ser mayor que homepage"}, status.HTTP_400_BAD_REQUEST
        )
    elif final_page > pages_max:
        return Response(
            {"error": f"final_page debe ser menor a {pages_max}"}, status.HTTP_400_BAD_REQUEST
        )
    else:
        data_file, page, last_page = data_injection_from_scraper(homepage, final_page)
        if int(last_page) > homepage:
            return Response(
                {"error": f"La ultima pagina scrapeada fue pag. {int(last_page)}"},
                status.HTTP_400_BAD_REQUEST,
            )
        if page != final_page:
            return Response(
                {"message": f"Se detuvo el scrapeo en la pagina {page}"}, status.HTTP_200_OK
            )
        return Response(data_file, status.HTTP_200_OK)
