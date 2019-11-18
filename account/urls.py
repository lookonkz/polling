from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
from .views import register
from django.urls import reverse_lazy
# from allauth.account.views import LogoutView
from django.contrib.auth import logout

app_name = 'account'
urlpatterns = [
    path('logout/', logout_then_login, name='account_logout'),
    # path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='account/registration/logged_out.html'), name='logout'),
    # path('logout-then-login/', logout_then_login, name='logout_then_login'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(
    #     template_name='account/password_change_form.html', success_url=reverse_lazy('account:password_change_done')),
    #      name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='account/password_change_done.html'), name='password_change_done'),
]
