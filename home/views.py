from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ContactMessage, NewsletterSubscriber, Review
from django.core.mail import send_mail

def home(request):
    reviews = Review.objects.order_by("-created_at")[:10]
    return render(request, "index.html", {"reviews": reviews})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        return JsonResponse({"success": True})

    return render(request, "contact.html")

@login_required
def faq(request):
    faqs = [
        {
            "q": "How long does delivery take?",
            "a": "We ship most orders within 5-7 business days. Express delivery is available."
        },
        {
            "q": "Can I return my order?",
            "a": "Yes, we offer a 30-day money-back guarantee on eligible products."
        },
        {
            "q": "What image formats do you accept?",
            "a": "We accept JPG, PNG, and GIF formats up to 5MB."
        },
        {
            "q": "Do you offer bulk or corporate orders?",
            "a": "Yes, we provide special pricing for bulk and corporate orders."
        },
        {
            "q": "Can I customize any product?",
            "a": "Most of our products can be customized with text, images, or dates."
        },
        {
            "q": "Do you offer gift wrapping?",
            "a": "Premium gift wrapping options are available during checkout."
        },
        {
            "q": "What payment methods do you accept?",
            "a": "We accept cards, PayPal, Apple Pay, and Google Pay."
        },
        {
            "q": "Can I send a gift directly to someone?",
            "a": "Yes, you can ship directly to the recipient with a personalized note."
        },
        {
            "q": "How do I track my order?",
            "a": "You'll receive a tracking link via email once your order is shipped."
        },
    ]
    return render(request, 'faq.html', {"faqs": faqs})

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if NewsletterSubscriber.objects.filter(email=email).exists():
            return JsonResponse({"status": "exists"})
        NewsletterSubscriber.objects.create(email=email)
        # Send confirmation email
        send_mail(
            subject="🎁 Welcome to LuxeGifts!",
            message=(
                "Thank you for subscribing to LuxeGifts!\n\n"
                "You'll now receive exclusive offers, gift ideas, and updates.\n\n"
                "— Team LuxeGifts"
            ),
            from_email=None,
            recipient_list=[email],
            fail_silently=True,
        )
        return JsonResponse({"status": "success"})
