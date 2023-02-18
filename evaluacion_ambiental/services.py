from evaluacion_ambiental.providers import get_data_by_url, creating_json_file_with_data, numbers_page
from evaluacion_ambiental.lib.constans import URL_EVALUACION_AMBIENTAL

def data_injection_from_scraper(homepage:int , final_page: int):
    """Updates the qualification associated to an especific lead - lead activity
    Args:
        qualification (int): Score (1-5) of lead buyer
        lead_activity_id (int): Id of lead activity"""
    data_file, page, last_page = creating_json_file_with_data(homepage, final_page)
    return data_file, page, last_page

def numbers_page_from_homepage():
    """Updates the qualification associated to an especific lead - lead activity
    Args:
        qualification (int): Score (1-5) of lead buyer
        lead_activity_id (int): Id of lead activity"""
    return numbers_page()
    
