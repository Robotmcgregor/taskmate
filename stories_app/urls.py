from django.urls import path
from stories_app import views as stories_view

urlpatterns = [
    path('', stories_view.stories, name='stories'),
    #path('profile-list/', stories_view.profile_list, name="profile_list"),



]