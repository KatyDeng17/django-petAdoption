from django.contrib import admin

# Register your models here.

from .models import Pet    # equal to import Pet from "./models"
# pd: learning123  for this app's djangosuppersure


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
