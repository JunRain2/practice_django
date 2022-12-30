from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # path에 'pybo/'가 생략된 것.
]