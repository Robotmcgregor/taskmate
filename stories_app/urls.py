from django.urls import path
from stories_app import views as stories_views

urlpatterns = [
    path('', stories_views.stories, name='stories'),



]