from django.contrib import admin
from .models import Region, Fruit

# Register your models here.

admin.site.register([Region,Fruit])