from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def send_welcome_email(name, email):
    # Customize the email content as per your requirements
    subject = "Welcome to Rapunzel Hair Affair"
    message = (
        f"Hello, {name},\n\n"
        f"Welcome to Rapunzel Hair Affair where beauty meets elegance! In accordance with our esteemed motto, we offer hairdressing, nail decoration, and massage services. Get to book one of the sessions to enjoy the services we render.\n\n"
        f"Our achievement is to have a satisfied customer.\n\n"
        f"Look your best, Feel your best\n\n"
        f"<a href='https://rapunzelhairaffair.com/' style='background-color: #4CAF50; color: white; padding: 14px 20px; text-align: center; text-decoration: none; display: inline-block;'>"
        f"Book Now"
        f"</a>\n"
    )
    from_email = "mashphotographer36@gmail.com"  # Update with your email
    recipient_list = [email]

    try:
        send_mail(subject, "", from_email, recipient_list, html_message=message)
        return True
    except Exception as e:
        return False

def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        if send_welcome_email(name, email):
            messages.success(request, f"A welcome email has successfully been sent to {email}. Check your email for more information.")
        else:
            messages.error(request, "Error sending email. Please try again.")

    return render(request, "index.html")
