from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.conf import settings 
from django.core.mail import EmailMessage

def index(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/index.html', {'current_year': current_year})

def faqs(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/faqs/faqs.html', {'current_year': current_year})

def blog(request):
    current_year = datetime.now().year
    return render(request, 'nabsil_website/blog/blog.html', {'current_year': current_year})

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        sender_email = request.POST['email']  # Changed variable name to avoid shadowing
        subject = request.POST['subject']
        message = request.POST['message']

        email_subject = f"Nabsil Grain Bank Contact Form Submission: {subject}"
        email_message = f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}"

        try:
            # Create an EmailMessage instance
            email = EmailMessage(
                subject=email_subject,
                body=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Ensure this is a valid, authenticated email address
                to=['info@nabsilgrainbank.com'],  # Recipient email
                reply_to=[sender_email],  # Use sender's email as reply-to
            )
            email.send()
            # Success message
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            # Error message
            messages.error(request, 'An error occurred while sending your message. Please try again later.')

        return redirect('contact')  # Redirect after POST to avoid form resubmission

    # Render the contact form page
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'nabsil_website/contact/contact.html', context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            # Create an EmailMessage instance for the newsletter subscription
            email_message = EmailMessage(
                subject="New Newsletter Subscription",
                body=f"A new user has subscribed to the newsletter with the email: {email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['info@nabsilgrainbank.com'],  # Set this to the email where you want to receive subscription notifications
                reply_to=[email],
            )
            email_message.send()
            # Success message
            messages.success(request, 'Your subscription request has been sent. Thank you!')
        except Exception as e:
            # Error message
            messages.error(request, 'An error occurred while processing your subscription. Please try again later.')

        return redirect('newsletter_subscribe')  # Redirect to a common page or specific URL

    # Render the index page with success/failure context
    context = {
        'scroll_to': 'footer',
        'current_year': datetime.now().year
    }
    return render(request, 'nabsil_website/index.html', context)

def blog_message(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            # Create an EmailMessage instance for the newsletter subscription
            email_message = EmailMessage(
                subject="New Newsletter Subscription",
                body=f"A new user has subscribed to the newsletter with the email: {email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['info@nabsilgrainbank.com'],  # Set this to the email where you want to receive subscription notifications
                reply_to=[email],
            )
            email_message.send()
            # Success message
            messages.success(request, 'Your subscription request has been sent. Thank you!')
        except Exception as e:
            # Error message
            messages.error(request, 'An error occurred while processing your subscription. Please try again later.')

        return redirect('blog_message')  # Redirect to a common page or specific URL

    # Render the index page with success/failure context
    context = {
        'scroll_to': 'footer',
        'current_year': datetime.now().year
    }
    return render(request, 'nabsil_website/blog/blog.html', context)

def faq_message(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            # Create an EmailMessage instance for the newsletter subscription
            email_message = EmailMessage(
                subject="New Newsletter Subscription",
                body=f"A new user has subscribed to the newsletter with the email: {email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['info@nabsilgrainbank.com'],  # Set this to the email where you want to receive subscription notifications
                reply_to=[email],
            )
            email_message.send()
            # Success message
            messages.success(request, 'Your subscription request has been sent. Thank you!')
        except Exception as e:
            # Error message
            messages.error(request, 'An error occurred while processing your subscription. Please try again later.')

        return redirect('faq_message')  # Redirect to a common page or specific URL

    # Render the index page with success/failure context
    context = {
        'scroll_to': 'footer',
        'current_year': datetime.now().year
    }
    return render(request, 'nabsil_website/faqs/faqs.html', context)

def contact_message(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            # Create an EmailMessage instance for the newsletter subscription
            email_message = EmailMessage(
                subject="New Newsletter Subscription",
                body=f"A new user has subscribed to the newsletter with the email: {email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['info@nabsilgrainbank.com'],  # Set this to the email where you want to receive subscription notifications
                reply_to=[email],
            )
            email_message.send()
            # Success message
            messages.success(request, 'Your subscription request has been sent. Thank you!')
        except Exception as e:
            # Error message
            messages.error(request, 'An error occurred while processing your subscription. Please try again later.')

        return redirect('contact_message')  # Redirect to a common page or specific URL

    # Render the index page with success/failure context
    context = {
        'scroll_to': 'footer',
        'current_year': datetime.now().year
    }
    return render(request, 'nabsil_website/contact/contact.html', context)