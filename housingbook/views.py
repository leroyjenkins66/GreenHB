from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Apartment, Consumption

# Create your views here.
def index(request):
    return HttpResponse("Welcome to #TeamSAS's green digital housing book!")
    
def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    latest_consumption_list = Consumption.objects.filter( apartment_id=apartment_id ).order_by('-reading_date')#[:5]
    
    context = {
        'apartment': apartment,
        'latest_consumption_list': latest_consumption_list,
    }
    
    return render(request, 'housingbook/detail.html', context)