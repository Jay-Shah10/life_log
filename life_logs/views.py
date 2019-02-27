from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, Entry
from .forms import EventForm, EntryForm

# Create your views here.
def index(request):
    """ Home page for  life log. This points to the html page. """
    return render(request, 'life_logs/index.html')

def events(request):
    """ Shows all Events"""
    events = Event.objects.order_by('date_added')
    context = {'events':events}
    return render(request, 'life_logs/events.html', context=context)

def topic(request, pk):
    """ Get individual Entries based on the Event. """
    topic = Event.objects.get(id=pk)
    entries = topic.entry_set.order_by('-date_added')
    context = {'event': topic, 'entries':entries}
    return render(request, 'life_logs/topic.html', context=context)


def new_event(request):
    """Add a new event"""
    if request.method != "POST":
        # NO dta submitted; created a blank form. 
        form = EventForm()
    else:
        # POST data submitted; process data
        form = EventForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('life_logs:events'))
    context = {'form':form}
    return render(request, 'life_logs/new_event.html', context)

def new_entry(request, event_id):
    """Add new Entry for an Event"""
    event = Event.objects.get(id=event_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data. 
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # saves it the post, but does not commit to the database.
            new_entry.event = event # links the post the event it is related to. 
            new_entry.save() # Now we save the post. 
            return HttpResponseRedirect(reverse('life_logs:topic', args=[event_id])) # shows the individual topic page with entries.
    context = {'event':event, 'form':form}
    return render(request, 'life_logs/new_entry.html', context)  # render the new_entry page. 