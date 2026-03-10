from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
# from views import todolist

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),
    
    path('account/', include('user_app.urls')),

]
