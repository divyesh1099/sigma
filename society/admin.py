from django.contrib import admin
from .models import *
# Register your models here.
class GeneralAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }
        js = ("js/richtext.js",)
admin.site.register(User)
admin.site.register(Profile, GeneralAdmin)
