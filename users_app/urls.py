from django.urls import path
#from . import views
from users_app import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('register/', user_views.register_user, name='register'),
    path('login/', user_views.login_user, name='login'),
    path('logout/', user_views.logout_user, name='logout'),
    path('profile/', user_views.profile, name="profile"),
    path('edit-profile/', user_views.edit_profile, name="edit_profile"),
    path('change-password/', user_views.change_password, name="change_password"),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)