from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    
    # Local Apps
    path('', include('games.urls')),
    path('', include('pages.urls')),
    path('reviews/', include('reviews.urls')),
]
