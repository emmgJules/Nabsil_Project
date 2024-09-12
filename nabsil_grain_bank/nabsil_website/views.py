from django.shortcuts import render
from datetime import datetime

def index(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/index.html', {'current_year': current_year})

def contact(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/contact/contact.html', {'current_year': current_year})

def faqs(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/faqs/faqs.html', {'current_year': current_year})

def blog(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/blog/blog.html', {'current_year': current_year})
