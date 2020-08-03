from django.shortcuts import render , redirect
from .forms import UserForm
from django.contrib.auth import logout, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/accounts/login')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

    return render(request , 'registration/register.html' , context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/news")






















# from django.shortcuts import render

# def register(request):
#     return render(request, 'register.html')


# def login(request):
#     return render(request, 'login.html')