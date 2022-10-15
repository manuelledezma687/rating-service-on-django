from datetime import time
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Rating


class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "latest_ratings_list"

    def get_queryset(self): 
        """Return the last five published questions (not including those set to be published in the future)."""
        return Rating.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:3]