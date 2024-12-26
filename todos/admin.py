from django.contrib import admin
from .models import(
    Task,
    TaskStatusChange,
    Why,
    Answer,
)
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskStatusChange)
admin.site.register(Why)
admin.site.register(Answer)
