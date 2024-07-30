from django.apps import AppConfig


class PortafolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.portafolio'    #se le debe agregar applications para que lo reconozca, puede que corra sin errores pero no aparezcan los modelos en el paneladmin
