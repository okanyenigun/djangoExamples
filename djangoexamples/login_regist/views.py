from .forms import UserForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginView(View):

    def get(self,request):
        form = UserForm()
        
        return render(request,'./templates/login_regist/login.html',{'form':form})
    
    def post(self,request):
        if "sign-in" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("pswd")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Login attemp failed.')
                return redirect('account_login')
            
        if "sign-up" in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                user = form.save()
                selected_group = request.POST.get("groups")
                group = Group.objects.get(name=selected_group)
                user.groups.add(group)
                messages.success(request,'Account has been created succesfully')
                return redirect('account_login')
            else:
                messages.error(request,form.errors)
                return redirect('account_login')
        return render(request,'./templates/login_regist/login.html')

class LogoutView(View):

    def get(self,request):
        logout(request)
        messages.success(request,'Logged out succesfully.')
        return redirect('account_login')

@method_decorator(login_required(login_url='login/'),name="dispatch")
class HomeView(View):
    def get(self,request):
        if self.request.user.groups.filter(name='M').exists():
            return render(request,'./templates/login_regist/home.html')
        else:
            messages.info(request,'You are not authorized to access this page.')
            return redirect('account_login')