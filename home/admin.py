from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber, Review

# CONTACT MESSAGES ADMIN
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )
    list_filter = (
        "subject",
        "created_at",
    )
    search_fields = (
        "name",
        "email",
        "message",
    )
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Sender Information", {
            "fields": ("name", "email", "phone")
        }),
        ("Message Details", {
            "fields": ("subject", "message")
        }),
        ("Metadata", {
            "fields": ("created_at",)
        }),
    )

# NEWSLETTER SUBSCRIBERS ADMIN
@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_active",
        "subscribed_at",
    )
    list_filter = (
        "is_active",
        "subscribed_at",
    )
    search_fields = (
        "email",
    )
    ordering = ("-subscribed_at",)
    readonly_fields = ("subscribed_at",)
    actions = ["deactivate_subscribers"]
    def deactivate_subscribers(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected subscribers have been deactivated.")
    deactivate_subscribers.short_description = "Deactivate selected subscribers"

# REVIEWS ADMIN
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "rating",
        "is_approved",
        "created_at",
    )
    list_filter = (
        "rating",
        "is_approved",
        "created_at",
    )
    search_fields = (
        "name",
        "message",
    )
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    actions = ["approve_reviews"]
    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected reviews approved successfully.")
    approve_reviews.short_description = "Approve selected reviews"
