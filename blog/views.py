from django.shortcuts import render
from .models import User, Skills, About, Accomplishments
from .forms import ContactMeForm
import smtplib




def index(request):
    form = ContactMeForm()
    user = User.objects.get(id=1)
    user_skills = user.skills.all()
    about = About.objects.get(id=1)
    accomplishments = Accomplishments.objects.all()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_message = f"Name: {name}\n\nEmail: {email}\n\nMessage: {message}"
            print(f"{name} - {email} - {subject} - {message}")
            send_email(subject, email_message, 'ahrorbek.xasanov@yahoo.com', recipient_list=['ahrorbek.xasanov@yahoo.com'], fail_silently=False)
            return redirect('index')
    else:
        form = ContactMeForm()

    context = {
        'user': user,
        'skills': user_skills,
        'info': about,
        'accomplishments': accomplishments,
        'form': form
    }
    return render(request, 'blog/index.html', context)