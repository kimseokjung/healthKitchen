from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.question_list, name='question_list'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('write', views.question_write, name='question_write'),
]