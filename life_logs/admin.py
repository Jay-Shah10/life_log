from django.contrib import admin
from .models import Event, Entry
# Register your models here.
# Adds the model to the admin page. 
admin.site.register(Event)
admin.site.register(Entry)
