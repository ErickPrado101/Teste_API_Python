 
from django.urls import path
from . import views
from .views import enviar_emails

urlpatterns = [
    path('emails/', views.EmailList.as_view(), name='email-list'),
    path('emails/<int:pk>/', views.EmailDetail.as_view(), name='email-detail'),
    path('enviar-emails/', enviar_emails, name='enviar_emails'),
]