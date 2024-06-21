from django.contrib.auth.models import AbstractUser
from django.db import models

# Модель пользователя
class User(AbstractUser):
    # Возможные роли пользователя
    ROLE_CHOICES = (
        ('менеджер', 'Менеджер'),
        ('сотрудник_обслуживания_номеров', 'Сотрудник обслуживания номеров'),
        ('сотрудник_предоставления_услуг', 'Сотрудник предоставления услуг отеля'),
    )
    # Возможные статусы пользователя
    STATUS_CHOICES = (
        ('работает', 'Работает'),
        ('уволен', 'Уволен'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)  # Роль пользователя
    first_name = models.CharField(max_length=30)  # Имя пользователя
    last_name = models.CharField(max_length=30)  # Фамилия пользователя
    father_name = models.CharField(max_length=30, default='-')  # Отчество пользователя
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='работает')  # Статус пользователя

# Модель заказа
class Order(models.Model):
    # Возможные статусы заказа
    STATUS_CHOICES = (
        ('в_процессе', 'В процессе'),
        ('готов', 'Готов'),
    )
    # Возможные статусы оплаты заказа
    PAYMENT_STATUS_CHOICES = (
        ('принят', 'Принят'),
        ('оплачен', 'Оплачен'),
    )
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)  # Создатель заказа
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing')  # Статус заказа
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления заказа
    details = models.TextField()  # Детали заказа
    room_num = models.CharField(max_length=7, default=1)  # Номер комнаты
    amount_clients = models.IntegerField(default=1)  # Количество клиентов
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')  # Статус оплаты

# Модель смены
class Shift(models.Model):
    user = models.ForeignKey(User, related_name='shifts', on_delete=models.CASCADE)  # Пользователь, которому назначена смена
    start_time = models.DateTimeField()  # Время начала смены
    end_time = models.DateTimeField()  # Время окончания смены

    def __str__(self):
        # Возвращает строковое представление смены
        return f"{self.user.username}: {self.start_time} - {self.end_time}"
