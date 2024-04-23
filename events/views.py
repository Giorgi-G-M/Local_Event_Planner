from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_detail(request, title):
    event = get_object_or_404(Event, title=title)
    return render(request, 'event_detail.html', {'event': event})