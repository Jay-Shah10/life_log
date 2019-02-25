from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, Entry
from .forms import EventForm

# Create your views here.
def index(request):
    """ Home page for  life log. This points to the html page. """
    return render(request, 'life_logs/index.html')

def events(request):
    """ Shows all Events"""
    events = Event.objects.order_by('date_added')
    context = {'events':events}
    return render(request, 'life_logs/events.html', context=context)

def entry(request, pk):
    """ Get individual Entries based on the Event. """
    entry = Event.objects.get(id=pk)
    entries = entry.entry_set.order_by('-date_added')
    context = {'event':entry, 'entries':entries}
    return render(request, 'life_logs/entry.html', context=context)

def new_event(request):
    """Add a new event"""
    if request.method != "POST":
        # NO dta submitted; created a blank form. 
        form = EventForm()
    else:
        # POST data submitted; process data
        form = EventForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('life_logs:events'))
    context = {'form':form}
    return render(request, 'life_logs/new_event.html', context)

