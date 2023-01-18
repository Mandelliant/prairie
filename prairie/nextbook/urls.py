from django.urls import path
from nextbook import views
from nextbook.views import suggestion

urlpatterns = [
    path(r'nextbook/', views.suggestion, name='suggestion'),
    path('', views.suggestion, name='suggestion'),
]