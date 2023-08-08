from django.contrib import messages
from django.shortcuts import render, redirect

from users.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('food:index')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})
