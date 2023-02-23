from django.apps import AppConfig


class EvaluacionAmbientalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evaluacion_ambiental'
    def ready(self):
        from evaluacion_ambiental.scheduler import worker
        worker.start()
