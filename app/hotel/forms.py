# hotel/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order, Shift

# Форма для регистрации пользователя
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']  # Поля формы
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'role': 'Должность',
        }

# Форма для создания/редактирования заказа
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['details', 'status', 'payment_status', 'amount_clients', 'room_num']  # Поля формы
        labels = {
            'details': 'Детали заказа',
            'status': 'Статус заказа',
            'payment_status': 'Статус оплаты',
            'amount_clients': 'Количество клиентов',
            'room_num': 'Номер комнаты',
        }

# Форма для назначения смен
class ShiftAssignmentForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['user', 'start_time', 'end_time']  # Поля формы
        labels = {
            'user': 'Сотрудник',
            'start_time': 'Начало смены',
            'end_time': 'Конец смены',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтрация пользователей по роли и статусу для выбора в форме
        self.fields['user'].queryset = User.objects.filter(role__in=['сотрудник_обслуживания_номеров', 'сотрудник_предоставления_услуг'], status='работает')

# Расширенная форма регистрации пользователя
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role', 'first_name', 'last_name', 'father_name', 'status']  # Поля формы
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'role': 'Должность',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'father_name': 'Отчество',
            'status': 'Статус',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].initial = 'active'  # Установка начального значения статуса

# Форма для изменения статуса оплаты заказа
class OrderStatusPaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_status']  # Поле формы
        read_only_fields = ['room_num', 'amount_clients', 'hotel_services', 'status']  # Поля только для чтения

# Форма для изменения статуса заказа
class OrderStatusOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']  # Поле формы
        read_only_fields = ['room_num', 'amount_clients', 'hotel_services', 'order_status']  # Поля только для чтения
