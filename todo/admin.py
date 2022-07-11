from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class DriverAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class DriverAdmin(admin.ModelAdmin):
    pass
