from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadastra, name='cadastro'),
]
