from django.apps import AppConfig

# Конфигурация приложения "Hotel"
class HotelConfig(AppConfig):
    # Поле по умолчанию для автоинкрементного первичного ключа
    default_auto_field = 'django.db.models.BigAutoField'
    # Имя приложения
    name = 'hotel'
