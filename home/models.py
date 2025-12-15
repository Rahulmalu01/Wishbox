from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# CONTACT MESSAGES
class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ("order", "Order Question"),
        ("product", "Product Inquiry"),
        ("customization", "Customization Help"),
        ("bulk", "Bulk Orders"),
        ("feedback", "Feedback"),
        ("other", "Other"),
    ]
    name = models.CharField(
        max_length=100,
        verbose_name="Full Name"
    )
    email = models.EmailField(
        db_index=True,
        verbose_name="Email Address"
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES
    )
    message = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now
    )
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    def __str__(self):
        return f"{self.name} | {self.get_subject_display()}"

# NEWSLETTER SUBSCRIBERS
class NewsletterSubscriber(models.Model):
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Subscriber Email"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Unsubscribe support"
    )
    subscribed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-subscribed_at"]
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"

    def __str__(self):
        return self.email or "No Email (Legacy Entry)"

# CUSTOMER REVIEWS
class Review(models.Model):
    name = models.CharField(
        max_length=100
    )
    message = models.TextField()
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    is_approved = models.BooleanField(
        default=True,
        help_text="Control visibility on website"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Customer Review"
        verbose_name_plural = "Customer Reviews"
    def __str__(self):
        return f"{self.name} ({self.rating}★)"
