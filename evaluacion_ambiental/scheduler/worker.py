from apscheduler.schedulers.background import BackgroundScheduler
from evaluacion_ambiental.providers import creating_json_file_with_data, numbers_page


def work_data_injection_from_scraper():
    end_page = numbers_page()
    data_file, page, last_page = creating_json_file_with_data(1, end_page)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(work_data_injection_from_scraper,'cron',hour = 21,minute=14, timezone = 'America/Lima')
    scheduler.start()
 