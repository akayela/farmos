from django.urls import path
from . import views

app_name = 'userauths'

urlpatterns = [
    path('', views.register_view, name='sign_up')
]

