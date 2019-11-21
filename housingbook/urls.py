from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_apartment/', views.my_apartment, name='my_apartment'),
    path('detail/<int:apartment_id>/', views.detail, name='detail'),
    path('operatoroverview/', views.op_overview, name='op_overview'),
    
    path('privacy/', TemplateView.as_view(template_name='housingbook/privacy.html'), name='privacy'),
]