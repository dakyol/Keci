from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name="logout"), #aslında burada herhangi bir template sağlamamıza gerek yok -hatta sağlamamalıyız ki bu url'e gidildiğinde herhangi bir sayfa açılmasın- çünkü 'logout' yapanları doğrudan 'keci_home'a yönlendiriyoruz.
    path('password_change/', login_required(auth_views.PasswordChangeView.as_view(template_name='registration/custom_password_change_form.html', success_url="done"), login_url="/login/"), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/custom_password_change_done.html'), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', html_email_template_name='registration/custom_password_reset_email.html', subject_template_name='registration/custom_password_reset_subject.txt', success_url='done'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/custom_password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/custom_password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/custom_password_reset_complete.html'), name="password_reset_complete"),
]

