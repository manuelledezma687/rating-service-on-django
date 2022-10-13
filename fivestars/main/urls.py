from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    #ex: /ratings/
    path('', views.IndexView.as_view(), name='index'),
    
]