from django.urls import path, include
from . import views

app_name = 'life_logs'
urlpatterns = [
    # Homepage of life logs.
    path('', views.index, name='index'),

    # Show all Events.
    path('events/', views.events, name='events'),

    # Show an individual entry for an event. 
    path('events/<int:pk>/', views.entry, name='entry'),

    # Page for adding new Events. 
    path('new_event/', views.new_event, name='new_event'),
]