from django.urls import path, include
from . import views

app_name = 'wam'

urlpatterns = [
    path('', views.all_wams, name='all_wams'),
    path('<int:wam_id>/', views.detail, name='detail'),
]