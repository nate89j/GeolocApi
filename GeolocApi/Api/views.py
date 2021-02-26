from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests

def viewother(request):
    response = requests.get('http://api.ipstack.com/79.130.82.6?access_key=df4e81050c5f828e2fa0e228de5a27d2').json()
    return render(request, 'viewother.html', {'response':response})

@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome"}
    return JsonResponse(content)

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

# @csrf_exempt
# def restcall(request):
#     if request.method == 'POST':
#         r = requests.post('http://127.0.0.1:8000/api/test/', data=request.POST)
#     else:
#         r = requests.get('http://127.0.0.1:8000/api/test/', data=request.GET)

#     if r.status_code == 200 and request.method == 'POST':
#         # Convert response into dictionary and create Appointment
#         data = r.json()
#         # Construct required dictionary
#         appointment_attrs = {
#             "clinicId": data["some-key-that-points-to-clinicid"],
#             "time": data["some-key-that-points-to-time"],
#             "queueNo": data["some-key-that-points-to-queue-num"]
#         }
#         appointment = Appointment.objects.create(**appointment_attrs)
#         # r.text, r.content, r.url, r.json
#         return HttpResponse(r.text)
#     elif r.status_code == 200:  # GET response
#         return HttpResponse(r.text)

#     return HttpResponse('Could not save data')