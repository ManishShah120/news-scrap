from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register,
    logout_request,
)
app_name = 'accounts'

urlpatterns = [
    path('register/' , register , name='register'),
    path('logout/' , logout_request, name='logout'),
    # All this below part came from default auth_views so these are not required anymore
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   

]



# accounts/ logout/ [name='logout']
 # path('reset/<uidb64>/<token>/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('reset/done/', auth_views.PasswordChangeView.as_view(), name='password_change'),