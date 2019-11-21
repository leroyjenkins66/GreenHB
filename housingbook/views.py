from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Apartment, Consumption

@login_required
def index(request):
    return render(request, 'housingbook/index.html')

@login_required
def my_apartment(request):         
    #get the apartment just for the current user
    apartments = Apartment.objects.filter( user=request.user )
    
    if len(apartments) == 0: #use len instead of count to save one database access. count would have generated a SELECT COUNT(*) query, which is extra load on the db.
    #TODO: The db might be faster to get the number of rows. Do some profiling
        # handle error and ask user to ask operator to link them
        return render(request, 'housingbook/index.html')
        
    #there will only be one apartment.
    apartment = apartments.first()
        
    latest_consumption_list = Consumption.objects.filter( apartment_id=apartment.id ).order_by('-reading_date')#[:5]

    context = {
        'apartment': apartment,
        'latest_consumption_list': latest_consumption_list,
    }
    
    return render(request, 'housingbook/detail.html', context)
  
@staff_member_required  
def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    
    context = {
        'apartment': apartment,
    }
    
    return render(request, 'housingbook/detail.html', context)
    
@staff_member_required
def op_overview(request):
    apartments = Apartment.objects.all()
    
    context = {
        'apartment_list': apartments,
    }
    return render(request, 'housingbook/op_overview.html', context)