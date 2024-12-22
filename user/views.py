from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import redirect, render

from user.models import User


# Create your views here.
def register(request):
    if request.method=='POST':
        phone_number=request.POST['phone_number']
        password=request.POST['password']
        if phone_number.startswith('+998') and len(phone_number) == 17:
            phone_number = phone_number[5:]
        else:
            return JsonResponse({'success': False, 'message': 'Invalid phone number format!'})
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        users=User.objects.create(phone_number=phone_number,password=make_password(password))
        users.save()
        return redirect("home")
    return render(request,'home/index.html')




