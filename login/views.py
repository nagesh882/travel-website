from django.shortcuts import render, redirect
from .models import Account
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail


def generate_otp():
    return str(random.randint(100000, 999999))


def login(request):
    if request.method == 'POST':
        enter_email = request.POST['email']

        try:
            store_email = Account.objects.get(email_id = enter_email)
        except Account.DoesNotExist:
            return HttpResponse("<center><h1 style='color: red; margin-top: 150px'>Error: 404 Page Not Found</h1></center>")
        
        context = {
            'enter_email':enter_email,
            'store_email':store_email.email_id
        }
        
        OTP = generate_otp()

        email_subject = f'This message for OTP verification'
        email_message = f'Use following one time password for login...\n\n{OTP}'

        send_mail(
            email_subject,
            email_message,
            '{{store_email}}',
            [enter_email],
            fail_silently=False
        )

        request.session['OTP'] = OTP
        request.session['enter_email'] = enter_email

        return redirect('otp_verify')

    return render(request, 'login.html')

def otp_verify(request):
    return render(request, 'otp_verify.html')

@login_required()
def home(request):
    return render(request, 'index.html')