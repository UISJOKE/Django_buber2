from django.contrib import admin
from app.core.models import User, Car, Model, Type, CarNumber


admin.site.register(User)
admin.site.register(Car)
admin.site.register(Model)
admin.site.register(Type)

@admin.register(CarNumber)
class CarNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'number', 'series', 'region')
    actions = None
