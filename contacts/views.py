from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        creation_id = request.POST['creation_id']
        creation = request.POST['creation']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        creator_email = request.POST['creator_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                creation_id=creation_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this creation')
                return redirect('/creations/'+creation_id)

        contact = Contact(creation=creation, creation_id=creation_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # # Send mail
        # send_mail(
        #     'Creation Listing Inquiry',
        #     'There has been an inquiry for ' + creation +
        #     '. Sign into the admin panel for more info.', 'weizhang3581@gmail.com',
        #     [creator_email, 'emiliezhang@hotmail.ca'],
        #     fail_silently=False
        # )

        messages.success(
            request, 'Your request has been submitted, a creator will get back to you soon')
        return redirect('/creations/'+creation_id)
