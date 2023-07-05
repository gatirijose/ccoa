from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["full_name"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email,
                          ["wawerugatiri@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('home')
        messages.success(
            request, "Success! Message was successfully submited.")
    return render(request, 'sendemail/email.html', {"form": form})


def success_view(request):
    messages.add_message(
        request, "Success! Message was successfully submited.")
