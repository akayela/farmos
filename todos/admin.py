from django.contrib import admin
from .models import(
    Task,
    Status,
    Analysis,
)
# Register your models here.

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Analysis)
