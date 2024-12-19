from django.urls import path
from . import views
# from django.conf.urls.static import static
# from django.conf import settings
# from eshopApp.views import login

urlpatterns =[
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
]
