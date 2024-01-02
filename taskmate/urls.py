from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('contact/', todolist_views.contact, name='contact'),
    path('about/', todolist_views.about, name='about'),
    
    path('account/', include('users_app.urls')),
    path('stories/', include('stories_app.urls')),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



