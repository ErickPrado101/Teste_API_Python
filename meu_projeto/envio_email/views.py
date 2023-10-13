from django.shortcuts import render
from rest_framework import generics
from .serializers import EmailSerializer
from django.contrib import admin
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Email

class EmailList(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

def enviar_emails(request):
    emails_nao_enviados = Email.objects.filter(sent=False)

    for email in emails_nao_enviados:
        send_mail(
            email.subject,
            email.message,
            'seu_email@gmail.com',  # Remetente
            [email.recipient],      # Destinatário
        )
        email.sent = True
        email.save()

    return JsonResponse({'message': 'E-mails enviados com sucesso!'})
