from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model
from .form import  UserRegistrationForm ,UserLoginForm ,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from .decorators import user_not_authenticated
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

@user_not_authenticated
def register(request):
    if request.user.is_authenticated:
        redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,f"A new account created {user.username}")
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
    else:
        form = UserRegistrationForm()
    return render(
        request = request,
        template_name='users/register.html',
        context={"form":form}
    )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request,'Logged out successfully')
    return redirect('homepage')

@user_not_authenticated
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        form =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            if user is not None:
                login(request,user)
                messages.success(request,f"Hello <b>{user.username}</b> you have logged in")
                return redirect("homepage")
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)

    
    form = AuthenticationForm(UserLoginForm)

    return render(
        request = request,
        template_name='users/login.html',
        context={"form":form}
    )

    
def profile(request,username):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST,request.FILES , instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request,f'{user_form.username},Your profile has been updated')
            return redirect("profile",user_form.username)
        for error in list(form.erroes.values()):
            messages.error(request,error)


    if request.method == "POST":
        pass
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
        request = request,
        template_name='users/login.html',
        context={"form":form}
    )
    return redirect("/")
         

