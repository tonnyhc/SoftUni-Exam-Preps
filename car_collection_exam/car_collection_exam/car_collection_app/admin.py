from django.contrib import admin

from car_collection_exam.car_collection_app.models import Profile, Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
