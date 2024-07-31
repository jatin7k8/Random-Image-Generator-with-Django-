from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime
from home.models import Contact # type: ignore
from django.contrib import messages
# Create your views here.
# def index(request):
#     # return HttpResponse("this is home page ")
#     return render(request, 'index.html')
def fetch_unsplash_images(request):
    client_id = '_joF1EyKESBUV__L2Jr9fIrEiM-xM87j6wn4i2gdqF4'
    url = f'https://api.unsplash.com/photos/random?client_id={client_id}&count=7'


    response = requests.get(url)
    images = response.json()

    context = {
        'images': images
    }
    
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("this is aboutpage")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is service page")
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone , desc = desc , date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    
    return render(request, 'contact.html') 
 
    # return HttpResponse("this is contact page")