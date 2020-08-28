#noinspection PyUnresolvedReferences
from django.contrib import admin
#noinspection PyUnresolvedReferences
from .models import Todo
# Register your models here.
admin.site.register(Todo)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','date','completed')
    list_filter = ('title')