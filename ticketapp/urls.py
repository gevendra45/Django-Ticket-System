from django.urls import path
from . import views
from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView

urlpatterns = [
    path('', TicketListView.as_view(), name = 'ticket-home'),
    path('req/<int:pk>', TicketDetailView.as_view(), name = 'ticket-detail'),
    path('req/new', TicketCreateView.as_view(), name = 'ticket-create'),
    path('req/<int:pk>/update/', TicketUpdateView.as_view(), name = 'ticket-update'),
    #path('newticket', views.newpost, name = 'ticket-new'), 
    #path('', views.thome, name = 'ticket-home'),
    path('about', views.tabout, name = 'ticket-about'), 
]