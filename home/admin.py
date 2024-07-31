from django.contrib import admin
from home.models import Contact # type: ignore

# Register your models here.
admin.site.register(Contact)