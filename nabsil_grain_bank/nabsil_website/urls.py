from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="index_page"),
    path('faqs',views.faqs, name="faqs"),
    path('contact',views.contact, name="contact"),
    path('blog',views.blog, name="blog"),
]
