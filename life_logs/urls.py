from django.urls import path, include
from . import views

app_name = 'life_logs'
urlpatterns = [
    # Homepage of life logs.
    path('', views.index, name='index'),

    # Show all Events.
    path('events/', views.events, name='events'),

    # Show an individual entry for an event. 
    path('events/<int:pk>/', views.topic, name='topic'),

    # Page for adding new Events. 
    path('new_event/', views.new_event, name='new_event'),

    # page for new entries.
    path('new_entry/<int:event_id>/', views.new_entry, name='new_entry'),

    # To edit entry.
    path("edit_entry/<int:entry_id>/", views.edit_entry, name='edit_entry'),

    # To delete entry.
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    
]