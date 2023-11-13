from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('home/', views.welcome_view, name='welcome'),
]
