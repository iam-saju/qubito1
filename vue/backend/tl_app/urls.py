from django.contrib import admin
from django.urls import path, include
from .views import upload,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload, name='upload'),
    path('login/',login,name='login')
   
]
