from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('psw')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('success')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def success(request):
    return render(request, 'success.html')