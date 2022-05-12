from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from .decoretors import unauthenticated_user
from .models import Account
import requests
from booking.models import BookSlot

# Create your views here.


@unauthenticated_user
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(request,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')

            url = request.META.get("HTTP_REFERER")
            try:
                query = requests.utils.urlparse(url).query       # query=    next= /cart/checkout/
                params =  dict(  x.split('=') for x in query.split('&'))     #param :  {'next': '/cart/checkout'}
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except Exception as e:
                print("exception : ",e)

            return redirect('dashboard')
        else:
            messages.warning(request,'invalid crediantions')
            return redirect('login')

    return render(request,'accounts/login.html')



# we cannot create a func name as logout # becaause django has inbuilt logout fun
def logout_user(request):
    logout(request)
    return redirect('home')



@unauthenticated_user
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        user_name=email.split('@')[0]

        if password==confirm_password and password!='':
            if  Account.objects.filter(username=user_name).exists():
                messages.warning(request,'username exists')
                return redirect('register')
            else:
                if Account.objects.filter(email=email).exists() :
                    messages.warning(request,'email already exists')
                    return redirect('register')
                else:

                    user=Account.objects.create_user(username=user_name,email=email,password=password)
                    user.first_name=first_name
                    user.last_name=last_name
                    user.save()

                    messages.success(request,"Account created successfuly")
                    return redirect('login')

        else:
            messages.warning(request,'password do not match')
            return redirect('register')


    return render(request,'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    context ={}
    try :
        bookings = BookSlot.objects.filter(user=request.user).order_by('-id')
        context['bookings'] = bookings
        
    except Exception as e:
        messages.error(request,'something went wrong, Please try after sometime.')
        print('exception : ',e)

    return render(request,'accounts/dashboard.html', context)




@login_required(login_url='login')
def profile(request):
    data={}

    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']

        if request.FILES:
            profile_image=request.FILES['profile_image']
            request.user.profile_image=profile_image

        request.user.first_name=first_name
        request.user.last_name=last_name
        request.user.save()

        messages.success(request,'profile updated successfully')
        return render(request,'accounts/profileform.html')

    else :
        return render(request,'accounts/profileform.html')




