from django.shortcuts import render, redirect

def index(request):
    return render(request, 'nabsil_website/index.html')

