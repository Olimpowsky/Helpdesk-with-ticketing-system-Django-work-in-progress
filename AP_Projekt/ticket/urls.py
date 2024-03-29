from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('update-ticket/<int:pk>/', views.update_ticket, name='create-ticket'),
    path('ticket-details/<int:pk>/', views.ticket_details, name='ticket-details'),
    path('all-tickets/', views.all_tickets, name='all-tickets'),
    path('ticket-queue/', views.ticket_queue, name='ticket-queue'),
    path('accept-ticket/<int:pk>/', views.accept_ticket, name='accept-ticket'),
    path('close-ticket/<int:pk>/', views.close_ticket, name='close-ticket'),
    path('workspace/', views.workspace, name='workspace'),
    path('all-closed-tickets/', views.all_closed_tickets, name='all-closed-tickets')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)