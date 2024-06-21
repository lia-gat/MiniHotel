from django.urls import path, reverse_lazy
from hotel.views import register_user, dismiss_user, assign_shift, view_orders, create_order, change_order_status, home, view_shifts, user_list, fire_user
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user, name='register_user'),
    path('dismiss/<int:user_id>/', dismiss_user, name='dismiss_user'),
    path('assign_shift/', assign_shift, name='assign_shift'),
    path('view_shifts/', view_shifts, name='view_shifts'),
    path('orders/', view_orders, name='view_orders'),
    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:order_id>/status/<str:status>/', change_order_status, name='change_order_status'),
    path('', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page=reverse_lazy('login')
    ), name='logout'),
    # path('login/', auth_views.LoginView.as_view(authentication_form=AuthenticationForm, redirect_authenticated_user=True), name='login'),
    path('login/', auth_views.LoginView.as_view(authentication_form=AuthenticationForm, redirect_authenticated_user=True), name='login'),

    path('user_list/', user_list, name='user_list'),
    path('fire_user/<int:user_id>/', fire_user, name='fire_user'),
    # path('orders/<int:orderid>/preparation_status/', order_preparation_status_update, name='order_preparation_status_update'),
    # path('orders/<int:orderid>/payment_status/', order_payment_status_update, name='order_payment_status_update'),
]
