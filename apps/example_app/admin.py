from django.contrib import admin
from .models import UserProfile, Message  # Import the correct models

# Register the models with the admin site
admin.site.register(UserProfile)
admin.site.register(Message)
