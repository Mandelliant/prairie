from django.urls import path
from . import views
from newbook.views import library

urlpatterns = [
    path(r'newbook/', views.library, name='library'),
    path('', views.library, name='library'),
    path(r'?actions=newbook', views.library, name='library'),
]