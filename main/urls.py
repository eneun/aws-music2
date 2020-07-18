from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('s3_setting', views.s3_setting, name='s3_setting'),
    path('rds_setting', views.rds_setting, name='rds_setting'),
]