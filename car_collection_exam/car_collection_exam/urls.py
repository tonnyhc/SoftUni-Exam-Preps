
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('car_collection_exam.car_collection_app.urls')),
    path('admin/', admin.site.urls),
]
