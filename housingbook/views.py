from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Apartment, Consumption

@login_required
def apt_list(request):            
        apartments = Apartment.objects.filter( user=request.user )
        
        context = {
            'apt_list': apartments,
        }
        
        return render(request, 'housingbook/apt_list.html', context)
   
def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    latest_consumption_list = Consumption.objects.filter( apartment_id=apartment_id ).order_by('-reading_date')#[:5]
    
    context = {
        'apartment': apartment,
        'latest_consumption_list': latest_consumption_list,
    }
    
    return render(request, 'housingbook/detail.html', context)