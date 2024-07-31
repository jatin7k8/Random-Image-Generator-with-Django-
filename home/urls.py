from django.contrib import admin
from django.urls import path, include
from home import views# type: ignore

urlpatterns = [
    path('', views.fetch_unsplash_images, name = 'home'),
    path('about', views.about, name = 'about'),
    path('services', views.services, name = 'services'),
    path('contact', views.contact, name = 'contact'),

]
