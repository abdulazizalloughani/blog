from django.contrib import admin

# Register your models here.
from .models import post 

class postadmin(admin.ModelAdmin):
    list_display = ('title', 'states' , 'created_at')
    list_filter = ('states', 'created_at')
    search_fields = ['title', 'body',]
admin.site.register(post , postadmin)
