from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="index_page"),
    path('faqs',views.faqs, name="faqs"),
    path('contact',views.contact_form, name="contact"),
    path('blog',views.blog, name="blog"),
    path('newsletter', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('blog_message', views.blog_message, name='blog_message'),
    path('faq_message', views.faq_message, name='faq_message'),
    path('contact_message', views.contact_message, name='contact_message'),
]
