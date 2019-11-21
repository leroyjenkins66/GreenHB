from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')