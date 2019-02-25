from django import forms
from .models import Event, Entry

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['text']
        labels = {'text':''}


        

