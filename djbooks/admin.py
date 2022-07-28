from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        ( 'Name', {'fields': ['name']}),
        ('Salutation', {'fields': ['salutation']}),
        ('Email', {'fields': ['email']},)  
        ]
admin.site.register(Author, AuthorAdmin)
# Register your models here.
