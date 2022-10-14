from datetime import time
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import Booking
from .models import Rating


class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "latest_ratings_list"

    def get_queryset(self): 
        """Return the last five published questions (not including those set to be published in the future)."""
        return Rating.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:3]
    
    
def booking(request):
    if request.method == 'POST':
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
            pick_up = form.cleaned_data['pick_up']
            destiny = form.cleaned_data['destiny']
            full_name = form.cleaned_data['full_name']
            email= form.cleaned_data['email']
            flight = form.cleaned_data['flight']
            date = form.cleaned_data['date']
            date_time = form.cleaned_data['date_time']
            payment_method = form.cleaned_data['payment_method']
            type_of_travel = form.cleaned_data['type_of_travel']            
            observations = form.cleaned_data['observations']
            passengers = form.cleaned_data['passengers']
            messages.success(request, 'Booking created')
            return redirect('index')
        else:
            form =Booking()
        context = {'form': form}
        return render(request, 'main/index.html', context)