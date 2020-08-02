from django.shortcuts import render , redirect
from .forms import UserForm

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



























# from django.shortcuts import render

# def register(request):
#     return render(request, 'register.html')


# def login(request):
#     return render(request, 'login.html')