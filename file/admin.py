from django.contrib import admin
from .models import profilemodel
# Register your models here.

@admin.register(profilemodel)
class forumAdmin(admin.ModelAdmin):
    
    fields = ['__all__']
