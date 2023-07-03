from django.contrib import admin

from colors.models import ColorBox

# Register your models here.

@admin.register(ColorBox)
class ColorBoxAdmin(admin.ModelAdmin):
    list_display = ["color", "user"]
    list_filter = ["user"]
