from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from . models import Users

# Create your views here.

def index(request):
  
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    phone_number = request.POST.get('phone_number')
    password = request.POST.get('password')
    pic = request.POST.get('pic')
    date = request.POST.get('date')
    
    
    # create an object
    
    new_user = Users(first_name=first_name, last_name=last_name, email=email, age=age, gender=gender, phone_number=phone_number, password=password, date=date, pic=pic)
    new_user.save()
  
  # get all persons
  user = Users.objects.all()
  

  return render (request, 'index.html', {'user': user})
