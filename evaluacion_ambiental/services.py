from evaluacion_ambiental.providers import (
    creating_json_file_with_data,
    numbers_page,
)
from typing import Any, Dict, List, Tuple


def data_injection_from_scraper(
    homepage: int, final_page: int
) -> Tuple[List[Dict[str, Any]], int, float]:
    """
    The data from the scraper is injected into the database and creating json file

    Attributes:
        homepage -- (int) Number of the first page to scrape
        final_page -- (int) Number of the last page to scrape

    Return data in json format.
    """
    data_file, page, last_page = creating_json_file_with_data(homepage, final_page)
    return data_file, page, last_page


def numbers_page_from_homepage() -> int:
    """
    Number of pages to scrape

    Attributes:
        None --

    Return (int) number of urls
    """
    return numbers_page()
