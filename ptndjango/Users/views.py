from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout

from .forms import *
from .models import User

# Create your views here.
class UsersHome(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'userHome.html', {'users': users})
    
class UsersUser(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        if user:
            return render(request, 'userUser.html', {'user': user})
        else:
            return render(request, 'userUser.html', {'user': {}})
    
class UsersCreate(LoginRequiredMixin, View):
    def get(self, request):
        uf = CreateUserForm()
        return render(request, 'userCreate.html', {'form': uf})
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        newUser = User.objects.create_user(name=name, email=email, password=password, avatar=request.FILES.get('avatar'))
        return redirect(newUser)

class UsersUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        form = UpdateUserForm(instance=user)
        return render(request, 'userUpdate.html', {'form': form, 'user': user})
    def post(self, request, id):
        user = User.objects.get(id=id)
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            newUser = form.save()
            return redirect(newUser)
        else:
            return render(request, 'userUpdate.html', {'form': form, 'user': user})

class UsersDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'userDelete.html', {'user': user})
    def post(self, request, id):
        user = User.objects.get(id=id)
        user.delete()
        return redirect('users_home_url')
    
class UsersLogin(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, 'userLogin.html')
    
    def post(self, request):
        if request.method == 'POST':
            print("go")
            try:
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = User.objects.get(email=email)
                print(user)
                user = authenticate(request, email=email, password=password)
                print("user", user)
                login(request, user)
                print('user after all', user)
                return redirect('users_home_url')
            except:
                return render(request, 'userLogin.html', {'msg' :'Not correct login or password'})
        return render(request, 'usersLogin.html')
    
class UsersLogout(View):
    def get(self, request):
        return render(request, 'userLogout.html')
    
    def post(self, request):
        logout(request)
        return redirect('users_home_url')