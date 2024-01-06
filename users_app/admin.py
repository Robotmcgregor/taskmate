from django.contrib import admin
from django.contrib.auth.admin import Group, User
from .models import Profile
from users_app.models import Profile


# Mix the User and Profile models in admin.
class ProfileInline(admin.StackedInline):
    model = Profile
    #can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    
# Unregister the Group model from admin.
admin.site.unregister(Group)

# Extend the User model in admin.
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
# #     # Just display the username field.
# #     # list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
# #     # list_filter = ('is_active', 'is_staff', 'is_superuser')
# #     # search_fields = ('username', 'email', 'first_name', 'last_name')
# #     # ordering = ('username',)
# #     fields = ["username"]
    
# #     # Unregister the User model from admin.
# #     admin.site.unregister(User)
# #     # Register the User model with the new UserAdmin.
# #     admin.site.register(User, UserAdmin)

admin.site.unregister(User)
# Extend the Profile model in admin.
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)




