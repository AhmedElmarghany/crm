from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('create-record/', views.create_record, name='createrecord'),
    path('view/<int:record_id>/', views.view_record, name='view_record'),
    path('update/<int:record_id>/', views.update_record, name='update_record')
]