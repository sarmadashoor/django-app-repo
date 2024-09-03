from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Home Page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.example_app.urls')),
    path('', home_view),
]
