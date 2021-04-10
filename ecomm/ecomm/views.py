from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def registerPage(request):
        if request.user.is_authenticated:
		        return redirect('ShopHome')
        else:
  
                form = CreateUserForm()
                if request.method == 'POST':
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                            form.save()
                            user = form.cleaned_data.get('username')
                            messages.success(request, 'account was created' + user)

                            return redirect('logins')
                context={'form':form}
                return render(request, 'shop/register.html', context)
def loginPage(request):
        if request.user.is_authenticated:
	        return redirect('ShopHome')
        else:
                if request.method=='POST':
                        username = request.POST.get('username')
                        password = request.POST.get('password')

                        user = authenticate(request, username=username, password=password)

                        if user is not None:
                                login(request, user)
                                return redirect('ShopHome')
                        else:
                                messages.info(request, 'Username or password is incorrect')

                context={}
                return render(request, 'shop/login.html', context)

@login_required(login_url='logins')  
def index(request):
    return render(request, 'index.html')






