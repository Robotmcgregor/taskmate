from django.contrib import admin
from .models import Profile

# register the Profile model in users_app/admin.py so we can access Profile in our Admin panel.
admin.site.register(Profile)
