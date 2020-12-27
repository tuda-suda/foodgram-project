from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='auth/authForm.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='auth/logout.html'),
        name='logout'
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='auth/changePassword.html'
        ),
        name='password_change'
    ),
    path(
        'password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='auth/changePasswordDone.html'
        ),
        name='password_change_done'
    ),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='auth/resetPassword.html'
        ),
        name='password_reset'
    ),
    path(
        'password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/resetPasswordDone.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/resetPasswordConfirm.html'
        ),
        name='password_reset_confirm'
    ),
]
