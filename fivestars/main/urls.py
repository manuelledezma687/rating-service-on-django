from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    #ex: /main/
    path('', views.IndexView.as_view(), name='index'),
    path("", views.booking, name="booking"),
]