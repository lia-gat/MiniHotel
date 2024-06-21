from django.contrib import admin
from .models import User, Order, Shift

# Регистрация моделей в административной панели Django

# Регистрация модели User (пользователь)
admin.site.register(User)

# Регистрация модели Order (заказ)
admin.site.register(Order)

# Регистрация модели Shift (смена)
admin.site.register(Shift)
