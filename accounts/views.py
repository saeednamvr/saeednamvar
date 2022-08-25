from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterationForm
from django.contrib.auth.models import User


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create.user(cd['username'], cd['email'], cd['password'])
    else:
        form = UserRegisterationForm()
    return render(request, 'register.html', {'form':form})