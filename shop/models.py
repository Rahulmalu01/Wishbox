from django.db import models
from django.contrib.auth.models import User

class CustomOrder(models.Model):
    PRODUCT_CHOICES = [
        ("mug", "Personalized Mug"),
        ("tshirt", "Custom T-Shirt"),
        ("canvas", "Photo Canvas"),
        ("pillow", "Decorative Pillow"),
        ("blanket", "Photo Blanket"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
    custom_text = models.CharField(max_length=50, blank=True)
    text_color = models.CharField(max_length=20, default="#000000")
    text_font = models.CharField(max_length=50)
    packaging = models.CharField(max_length=20)
    gift_wrap = models.BooleanField(default=False)
    image = models.ImageField(upload_to="custom_uploads/", null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.total_price}"
