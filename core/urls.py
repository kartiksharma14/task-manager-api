from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # ✅ Add this line

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to Task Manager API")),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
