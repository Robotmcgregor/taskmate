from django.urls import path
#from users_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users_app import views as user_views


urlpatterns = [

    path('register/', user_views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    #path('login/', user_views.login_user, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    #path('profile/', auth_views.Profile.as_view(template_name='profile.html'), name="profile"),
    path('profile/', user_views.profile, name="profile"),
    path('edit-profile/', user_views.edit_profile, name="edit_profile"),


]



# ------------------- new code -------------------
# Only add this when we are in debug mode.
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

