from django.urls import path

from . import views

app_name = "ratings"

urlpatterns = [
    #ex: /ratings/
    path('', views.IndexView.as_view(), name='index'),
    
]