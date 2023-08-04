from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid:
            messages.success(request, 'El mensaje ah sido enviado correctamente')
            return redirect('home')
        else:
            messages.error(request, 'El mensaje no ah cumplido los requisitos')
            return redirect('contact')
    else:
        contact_form = ContactForm()
        
    return render(request, 'contact.html', {'contact_form':contact_form})