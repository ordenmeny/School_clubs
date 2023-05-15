from django.contrib import admin
from .models import PersonModel


# Register your models here.
class AdminPerson(admin.ModelAdmin):
    list_display = ('name', 'active', 'date_duty')


admin.site.register(PersonModel, AdminPerson)