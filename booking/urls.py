from django.urls import path
from . import views
app_name = 'booking'
urlpatterns = [path('', views.home, name='home'), path('done/<int:pk>/', views.success, name='success')]
