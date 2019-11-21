from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_apartment/', views.my_apartment, name='my_apartment'),
    path('detail/<int:apartment_id>/', views.detail, name='detail'),
    path('operatoroverview/', views.op_overview, name='op_overview'),
    
    path('privacy/', TemplateView.as_view(template_name='housingbook/privacy.html'), name='privacy'),

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]