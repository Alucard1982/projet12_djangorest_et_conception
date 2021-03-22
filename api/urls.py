from django.urls import path
from api import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),

    path('clients/', views.ClientListView.as_view()),
    path('clients/register', views.ClientCreateView.as_view()),
    path('clients/<int:pk>', views.ClientDetailView.as_view()),

    path('contrats/', views.ContratListView.as_view()),
    path('contrats/register', views.ContratCreateView.as_view()),
    path('contrats/<int:pk>', views.ContratDetailView.as_view()),
    path('clients/<int:pk>/contrats', views.ContratByClientListView.as_view()),

    path('events/', views.EventListView.as_view()),
    path('events/register', views.EventCreateView.as_view()),
    path('events/<int:pk>', views.EventDetailView.as_view()),
    path('clients/<int:pk>/events', views.EventByClientListView.as_view()),

    path('custom-registration/', views.CustomRegisterView.as_view()),
]
