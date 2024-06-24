from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, OrderForm, ShiftAssignmentForm
from .models import User, Order, Shift

@login_required
def register_user(request):
    # Проверка, что пользователь является менеджером
    if request.user.role  not in ['manager','менеджер']:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение нового пользователя
            return redirect('home')
    else:
        form = UserRegistrationForm()  # Создание пустой формы
    
    # Отображение страницы регистрации пользователя
    return render(request, 'hotel/register_user.html', {'form': form})

@login_required
def dismiss_user(request, user_id):
    # Проверка, что пользователь является менеджером
    if request.user.role  not in ['manager','менеджер']:
        return redirect('home')
    
    user = get_object_or_404(User, id=user_id)
    user.status = 'dismissed'  # Изменение статуса пользователя на "уволен"
    user.save()
    return redirect('register_user')  # Перенаправление на страницу регистрации пользователей

@login_required
def assign_shift(request):
    # Проверка, что пользователь является менеджером
    if request.user.role  not in ['manager','менеджер']:
        return redirect('home')
    


    if request.method == 'POST':
        form = ShiftAssignmentForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение новой смены
            return redirect('home')
    else:
        form = ShiftAssignmentForm()  # Создание пустой формы
    
    # Отображение страницы назначения смен
    return render(request, 'hotel/assign_shift.html', {'form': form})

@login_required
def view_shifts(request):
    # Проверка, что пользователь является менеджером
    if request.user.role not in ['manager','менеджер']:
        return redirect('home')
    

    shifts = Shift.objects.all()  # Получение всех смен
    # Отображение страницы просмотра смен
    return render(request, 'hotel/view_shifts.html', {'shifts': shifts})

@login_required
def view_orders(request):
    # Проверка, что пользователь имеет необходимую роль
    if request.user.role not in ['manager','менеджер',  'сотрудник_предоставления_услуг', 'сотрудник_обслуживания_номеров']:
        return redirect('home')
    
    orders = Order.objects.all()  # Получение всех заказов
    # Отображение страницы просмотра заказов
    return render(request, 'hotel/view_orders.html', {'orders': orders})


@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        # Здесь должна быть логика для обновления статуса заказа
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'hotel/update_order.html', {'form': form, 'order': order})

@login_required
def create_order(request):
    # Проверка, что пользователь имеет необходимую роль
    if request.user.role not in ['manager','менеджер', 'сотрудник_обслуживания_номеров']: 
        return redirect('home')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user  # Установка пользователя, создавшего заказ
            order.save()
            return redirect('home')
    else:
        form = OrderForm()  # Создание пустой формы
    
    # Отображение страницы создания заказа
    return render(request, 'hotel/create_order.html', {'form': form})
@login_required
def change_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    # Проверка, что пользователь имеет необходимую роль
    if request.user.role not in ['сотрудник_обслуживания_номеров', 'сотрудник_предоставления_услуг']:
        return redirect('home')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        # Проверка допустимости изменения статуса заказа в зависимости от роли пользователя
        if (request.user.role == 'сотрудник_обслуживания_номеров' and new_status in ['Принят', 'Оплачен']) or (request.user.role == 'сотрудник_предоставления_услуг' and new_status in ['В процессе', 'Готов']):
            order.status = new_status
            order.save()
            return redirect('view_orders')
    
    # Если метод не POST или статус не допустим, возвращаемся на страницу заказов
    return redirect('view_orders')

@login_required
def home(request):
    # Отображение домашней страницы
    return render(request, 'hotel/home.html')

@login_required
def user_list(request):
    users = User.objects.all()  # Получение всех пользователей
    # Отображение страницы со списком пользователей
    return render(request, 'hotel/user_list.html', {'users': users})

@login_required
def fire_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # Логика для изменения статуса пользователя на "уволен"
    user.status = 'уволен'
    user.save()
    return redirect('user_list')  # Перенаправление на страницу со списком пользователей
